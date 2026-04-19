import subprocess
import os
import time
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor

SKILL_PATH = Path(__file__).resolve().parents[1]
SKILLS_ROOT = Path(__file__).resolve().parents[3]
WORKSPACE = SKILLS_ROOT / "_workspaces" / "figma-variable-manager-workspace" / "iteration-1"
CLAUDE_COMMANDS_DIR = Path(".claude/commands")

evals = [
    {
        "id": 0,
        "name": "eval-0-single-color-update",
        "prompt": "Figma FileKey 是 'TEST_FILE_KEY', PAT 是 'YOUR_PAT'。请把 Mode 为 'Light' 下的 'brand/primary' 变量更新为 #FF5500。"
    },
    {
        "id": 1,
        "name": "eval-1-batch-update-multi-type",
        "prompt": "读取文件 'FILE_KEY2' 的变量。然后同步修改：1) 'radius/sm' 设为 8, 2) 'opacity/high' 设为 0.9, 3) 在 'Dark' 模式下将 'bg-page' 设为 #111111。"
    },
    {
        "id": 2,
        "name": "eval-2-error-handling-missing-variable",
        "prompt": "修改一个不存在的变量 'non-existent-var' 为 #000000。"
    }
]

def run_claude(prompt, output_file, with_skill=False):
    if with_skill:
        # Create skill command file
        CLAUDE_COMMANDS_DIR.mkdir(parents=True, exist_ok=True)
        skill_file = CLAUDE_COMMANDS_DIR / "figma-variable-manager.md"
        with open(SKILL_PATH / "SKILL.md", 'r') as f:
            skill_content = f.read()
        with open(skill_file, 'w') as f:
            f.write(skill_content)
        
        full_prompt = f"运用 figma-variable-manager 技能执行以下任务：{prompt}"
    else:
        full_prompt = prompt

    print(f"Starting: {output_file.parent.parent.name} ({'with_skill' if with_skill else 'baseline'})")
    
    start_time = time.time()
    try:
        # Remove CLAUDECODE to avoid nesting issues
        env = {k: v for k, v in os.environ.items() if k != "CLAUDECODE"}
        process = subprocess.run(
            ["claude", "-p", full_prompt],
            capture_output=True,
            text=True,
            env=env,
            timeout=120
        )
        duration = time.time() - start_time
        
        output_file.parent.mkdir(parents=True, exist_ok=True)
        with open(output_file, 'w') as f:
            f.write(process.stdout)
            f.write("\n\n--- STDERR ---\n")
            f.write(process.stderr)
        
        # Save timing
        timing_file = output_file.parent.parent / ("with_skill" if with_skill else "without_skill") / "timing.json"
        with open(timing_file, 'w') as f:
            import json
            json.dump({"duration_ms": int(duration * 1000), "total_duration_seconds": duration}, f)
            
        print(f"Finished: {output_file.parent.parent.name} in {duration:.2f}s")
    except Exception as e:
        print(f"Error running {output_file}: {e}")
    finally:
        if with_skill and (CLAUDE_COMMANDS_DIR / "figma-variable-manager.md").exists():
            (CLAUDE_COMMANDS_DIR / "figma-variable-manager.md").unlink()

def main():
    tasks = []
    for e in evals:
        eval_dir = WORKSPACE / e["name"]
        tasks.append((e["prompt"], eval_dir / "with_skill" / "outputs" / "output.txt", True))
        tasks.append((e["prompt"], eval_dir / "without_skill" / "outputs" / "output.txt", False))
    
    with ThreadPoolExecutor(max_workers=2) as executor:
        for t in tasks:
            executor.submit(run_claude, *t)

if __name__ == "__main__":
    main()
