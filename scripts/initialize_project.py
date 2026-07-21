"""
Project Initialization Script for Technical Diving Decompression Training
Automates setup of directories, configuration, and initial knowledge base seeding.
Production-grade with proper error handling and validation.

Usage:
    python scripts/initialize_project.py [--force] [--skip-deps]
"""

import argparse
import sys
import subprocess
from pathlib import Path
from typing import List, Tuple
import shutil


class ProjectInitializer:
    """Initialize project structure and dependencies"""

    def __init__(self, project_root: Path, force: bool = False, skip_deps: bool = False):
        self.project_root = project_root
        self.force = force
        self.skip_deps = skip_deps
        self.required_directories = [
            "skills",
            "tools",
            "tests",
            "config",
            "references",
            "assets",
            "scripts",
            "logs"
        ]
        self.required_files = [
            "CLAUDE.md",
            "PROJECT-detail.md",
            "PROJECT-DEVELOPMENT-PHASE-TRACKING.md",
            "README.md",
            "SECOND-KNOWLEDGE-BRAIN.md",
            "SKILL.md",
            "requirements.txt",
            "LICENSE"
        ]
        self.python_requirements = [
            "requests>=2.31.0",
            "feedparser>=6.0.10",
            "python-dateutil>=2.8.2",
            "structlog>=23.1.0"
        ]

    def create_directories(self) -> Tuple[bool, List[str]]:
        """Create required directory structure"""
        print("[INFO] Creating directory structure...")
        errors = []

        for dir_name in self.required_directories:
            dir_path = self.project_root / dir_name
            try:
                dir_path.mkdir(parents=True, exist_ok=True)
                print(f"  ✓ {dir_name}/")
            except Exception as e:
                error_msg = f"Failed to create {dir_name}/: {str(e)}"
                errors.append(error_msg)
                print(f"  ✗ {error_msg}")

        # Create .gitkeep in empty directories
        for dir_name in ["logs", "assets", "references"]:
            gitkeep = self.project_root / dir_name / ".gitkeep"
            if not gitkeep.exists():
                gitkeep.touch()

        return len(errors) == 0, errors

    def verify_files(self) -> Tuple[bool, List[str]]:
        """Verify required project files exist"""
        print("[INFO] Verifying required files...")
        missing = []

        for file_name in self.required_files:
            file_path = self.project_root / file_name
            if file_path.exists():
                print(f"  ✓ {file_name}")
            else:
                missing.append(file_name)
                print(f"  ✗ {file_name} (missing)")

        return len(missing) == 0, missing

    def install_dependencies(self) -> Tuple[bool, List[str]]:
        """Install Python dependencies"""
        if self.skip_deps:
            print("[INFO] Skipping dependency installation (--skip-deps)")
            return True, []

        print("[INFO] Installing Python dependencies...")
        errors = []

        try:
            # Create requirements.txt if not exists
            req_file = self.project_root / "requirements.txt"
            if not req_file.exists() or self.force:
                req_file.write_text("\n".join(self.python_requirements) + "\n")
                print(f"  ✓ Created requirements.txt")

            # Install packages
            result = subprocess.run(
                [sys.executable, "-m", "pip", "install", "-r", "requirements.txt"],
                cwd=self.project_root,
                capture_output=True,
                text=True
            )

            if result.returncode == 0:
                print("  ✓ All dependencies installed successfully")
                return True, []
            else:
                error_msg = f"pip install failed: {result.stderr}"
                errors.append(error_msg)
                print(f"  ✗ {error_msg}")
                return False, errors

        except Exception as e:
            error_msg = f"Dependency installation failed: {str(e)}"
            errors.append(error_msg)
            print(f"  ✗ {error_msg}")
            return False, errors

    def initialize_config(self) -> Tuple[bool, List[str]]:
        """Initialize configuration files"""
        print("[INFO] Initializing configuration...")
        errors = []

        try:
            # Copy default config if not exists
            default_config = self.project_root / "config" / "default_config.json"
            user_config = self.project_root / "config.json"

            if default_config.exists() and (not user_config.exists() or self.force):
                shutil.copy(default_config, user_config)
                print("  ✓ Created config.json")

            return True, []

        except Exception as e:
            error_msg = f"Config initialization failed: {str(e)}"
            errors.append(error_msg)
            print(f"  ✗ {error_msg}")
            return False, errors

    def initialize_git(self) -> Tuple[bool, List[str]]:
        """Initialize git repository if not already initialized"""
        print("[INFO] Checking git repository...")
        errors = []

        try:
            git_dir = self.project_root / ".git"
            if not git_dir.exists():
                result = subprocess.run(
                    ["git", "init"],
                    cwd=self.project_root,
                    capture_output=True,
                    text=True
                )
                if result.returncode == 0:
                    print("  ✓ Git repository initialized")
                else:
                    errors.append("git init failed")
                    print("  ✗ Failed to initialize git repository")
            else:
                print("  ✓ Git repository already exists")

            return True, []

        except Exception as e:
            error_msg = f"Git initialization failed: {str(e)}"
            errors.append(error_msg)
            print(f"  ✗ {error_msg}")
            return False, errors

    def run_validation(self) -> Tuple[bool, List[str]]:
        """Run project validation script"""
        print("[INFO] Running project validation...")
        errors = []

        try:
            validator = self.project_root / "tools" / "validate_project.py"
            if validator.exists():
                result = subprocess.run(
                    [sys.executable, str(validator)],
                    cwd=self.project_root,
                    capture_output=True,
                    text=True
                )
                if result.returncode == 0:
                    print("  ✓ Project validation passed")
                    return True, []
                else:
                    errors.append(f"Validation failed: {result.stderr}")
                    print(f"  ✗ {result.stderr}")
                    return False, errors
            else:
                print("  ⊙ Validator not found, skipping")
                return True, []

        except Exception as e:
            error_msg = f"Validation failed: {str(e)}"
            errors.append(error_msg)
            print(f"  ✗ {error_msg}")
            return False, errors

    def initialize(self) -> bool:
        """Run full initialization sequence"""
        print("=" * 60)
        print("TECHNICAL DIVING DECOMPRESSION TRAINING - PROJECT INITIALIZATION")
        print("=" * 60)
        print()

        success = True
        all_errors = []

        # Create directories
        ok, errors = self.create_directories()
        success = success and ok
        all_errors.extend(errors)

        # Verify files
        ok, errors = self.verify_files()
        success = success and ok
        all_errors.extend(errors)

        # Install dependencies
        ok, errors = self.install_dependencies()
        success = success and ok
        all_errors.extend(errors)

        # Initialize config
        ok, errors = self.initialize_config()
        success = success and ok
        all_errors.extend(errors)

        # Initialize git
        ok, errors = self.initialize_git()
        success = success and ok
        all_errors.extend(errors)

        # Run validation
        if success:
            ok, errors = self.run_validation()
            success = success and ok
            all_errors.extend(errors)

        # Summary
        print()
        print("=" * 60)
        if success:
            print("✓ INITIALIZATION COMPLETE")
            print("  Project is ready for development!")
        else:
            print("✗ INITIALIZATION INCOMPLETE")
            print("  Please address the following errors:")
            for error in all_errors:
                print(f"    - {error}")
        print("=" * 60)

        return success


def main():
    """Command-line interface"""
    parser = argparse.ArgumentParser(
        description="Initialize Technical Diving Decompression Training project"
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Force overwrite existing files"
    )
    parser.add_argument(
        "--skip-deps",
        action="store_true",
        help="Skip dependency installation"
    )

    args = parser.parse_args()

    # Determine project root
    project_root = Path(__file__).parent.parent

    # Run initialization
    initializer = ProjectInitializer(
        project_root=project_root,
        force=args.force,
        skip_deps=args.skip_deps
    )

    success = initializer.initialize()
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
