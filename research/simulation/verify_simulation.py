import os
import py_compile
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

FILES_TO_CHECK = [
    "simulation_engine_v4.py",
    "visualization_engine_v4.py",
    "generate_report_v4.py",
    "Algorapolis_Simulation_Report_V4.pdf",
    "simulation_results.json",
    "monte_carlo_stats.json",
    "pairwise_comparisons.json",
    "phase_analysis.json",
    "shock_log.json",
    "README.md",
    "requirements.txt"
]

SCRIPTS = [
    "simulation_engine_v4.py",
    "visualization_engine_v4.py",
    "generate_report_v4.py"
]

def check_file_existence():
    print("Checking file existence in research/simulation/...")
    all_exist = True
    for f in FILES_TO_CHECK:
        path = os.path.join(BASE_DIR, f)
        if not os.path.exists(path):
            print(f"FAIL: File missing: {f}")
            all_exist = False
        else:
            print(f"  OK: {f} exists")
            
    # Check charts
    charts_dir = os.path.join(BASE_DIR, "charts")
    if not os.path.isdir(charts_dir):
        print("FAIL: charts/ directory missing!")
        all_exist = False
    else:
        chart_files = [f for f in os.listdir(charts_dir) if f.endswith(".png")]
        print(f"  OK: Found {len(chart_files)} charts in charts/")
        if len(chart_files) != 28:
            print(f"FAIL: Expected 28 charts, found {len(chart_files)}")
            all_exist = False
            
    return all_exist

def verify_syntax():
    print("\nVerifying Python script compilation...")
    all_compiled = True
    for script in SCRIPTS:
        path = os.path.join(BASE_DIR, script)
        try:
            py_compile.compile(path, doraise=True)
            print(f"  OK: {script} compiled successfully")
        except py_compile.PyCompileError as e:
            print(f"FAIL: {script} compilation failed: {e}")
            all_compiled = False
    return all_compiled

def verify_paths():
    print("\nChecking for absolute hardcoded paths...")
    no_absolute_paths = True
    for script in SCRIPTS:
        path = os.path.join(BASE_DIR, script)
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        if "/home/z/my-project" in content:
            print(f"FAIL: Hardcoded path found in {script}")
            no_absolute_paths = False
        else:
            print(f"  OK: No absolute path found in {script}")
    return no_absolute_paths

def main():
    print("=== STARTING CIVILIZATION SIMULATION INTEGRATION VERIFICATION ===")
    exist_ok = check_file_existence()
    syntax_ok = verify_syntax()
    paths_ok = verify_paths()
    
    print("\n=== VERIFICATION SUMMARY ===")
    if exist_ok and syntax_ok and paths_ok:
        print("=== ALL VERIFICATION TESTS PASSED SUCCESSFULLY! ===")
        sys.exit(0)
    else:
        print("=== SOME VERIFICATION TESTS FAILED! ===")
        sys.exit(1)

if __name__ == "__main__":
    main()
