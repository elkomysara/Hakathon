"""
Quick Start Script for Research Opportunities Dashboard
Automatically sets up and launches the Streamlit dashboard
"""

import subprocess
import sys
import os
from pathlib import Path

def check_requirements():
    """Check if required packages are installed"""
    required_packages = {
        'streamlit': 'streamlit',
        'pandas': 'pandas',
        'plotly': 'plotly',
        'numpy': 'numpy'
    }
    
    missing_packages = []
    
    print("🔍 Checking required packages...")
    for package_name, import_name in required_packages.items():
        try:
            __import__(import_name)
            print(f"   ✅ {package_name} installed")
        except ImportError:
            print(f"   ❌ {package_name} missing")
            missing_packages.append(package_name)
    
    return missing_packages

def install_requirements(missing_packages):
    """Install missing packages"""
    if not missing_packages:
        return True
    
    print(f"\n📦 Installing missing packages: {', '.join(missing_packages)}")
    
    try:
        subprocess.check_call([
            sys.executable, "-m", "pip", "install", 
            "-r", "requirements_dashboard.txt"
        ])
        print("✅ All packages installed successfully!")
        return True
    except subprocess.CalledProcessError:
        print("❌ Failed to install packages. Please install manually:")
        print(f"   pip install {' '.join(missing_packages)}")
        return False

def check_data_file():
    """Check if the merged CSV exists"""
    csv_path = Path("/mnt/user-data/outputs/research_opportunities_merged.csv")
    
    if csv_path.exists():
        print(f"✅ Data file found: {csv_path}")
        return True
    else:
        print(f"❌ Data file not found: {csv_path}")
        print("\n⚠️  Please run merge_batches.py first to create the merged dataset:")
        print("   python merge_batches.py")
        return False

def launch_dashboard():
    """Launch the Streamlit dashboard"""
    print("\n🚀 Launching Streamlit dashboard...")
    print("="*60)
    print("📊 Dashboard will open in your default browser")
    print("🌐 URL: http://localhost:8501")
    print("🛑 Press Ctrl+C to stop the server")
    print("="*60)
    
    try:
        subprocess.run([
            sys.executable, "-m", "streamlit", "run",
            "streamlit_dashboard.py",
            "--server.headless", "false",
            "--server.port", "8501"
        ])
    except KeyboardInterrupt:
        print("\n\n👋 Dashboard stopped. Goodbye!")
    except Exception as e:
        print(f"\n❌ Error launching dashboard: {e}")
        print("\nTry running manually:")
        print("   streamlit run streamlit_dashboard.py")

def main():
    """Main execution function"""
    print("="*60)
    print("🎓 RESEARCH OPPORTUNITIES DASHBOARD - QUICK START")
    print("="*60)
    
    # Step 1: Check requirements
    missing = check_requirements()
    
    if missing:
        user_input = input("\n❓ Install missing packages? (y/n): ").lower()
        if user_input == 'y':
            if not install_requirements(missing):
                return
        else:
            print("⚠️  Cannot proceed without required packages.")
            return
    
    # Step 2: Check data file
    if not check_data_file():
        return
    
    # Step 3: Launch dashboard
    print("\n✅ All checks passed!")
    user_input = input("❓ Launch dashboard now? (y/n): ").lower()
    
    if user_input == 'y':
        launch_dashboard()
    else:
        print("\n📝 To launch manually, run:")
        print("   streamlit run streamlit_dashboard.py")
        print("\n👋 Goodbye!")

if __name__ == "__main__":
    main()
