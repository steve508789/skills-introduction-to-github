# API Documentation: GitHub Skills - Introduction to GitHub

This document provides comprehensive documentation for all public APIs, functions, and components in the "Introduction to GitHub" Skills exercise.

## Table of Contents

1. [Project Overview](#project-overview)
2. [GitHub Actions Workflows](#github-actions-workflows)
3. [Tutorial Steps API](#tutorial-steps-api)
4. [Automation Components](#automation-components)
5. [Usage Instructions](#usage-instructions)
6. [Configuration Reference](#configuration-reference)
7. [Examples](#examples)

## Project Overview

The "Introduction to GitHub" is an interactive tutorial that teaches new developers the fundamentals of GitHub through hands-on exercises. The project uses GitHub Actions workflows to automatically detect user progress and provide real-time feedback.

### Core Components

- **Automated Tutorial System**: Progressive learning with automated validation
- **GitHub Actions Workflows**: 5 main workflows that trigger on specific user actions
- **Step-by-step Instructions**: Markdown-based tutorial content
- **Real-time Feedback**: Automated comments and progress tracking

## GitHub Actions Workflows

### 1. Start Exercise Workflow

**File**: `.github/workflows/0-start-exercise.yml`

**Trigger**: Push to `main` branch

**Purpose**: Initializes the tutorial experience by creating an issue and posting the first step.

```yaml
name: Step 0 # Start Exercise
on:
  push:
    branches:
      - main
```

**Key Functions**:
- `start_exercise`: Creates tutorial issue using skills/exercise-toolkit
- `post_next_step_content`: Posts step 1 content to the issue
- Environment: `STEP_1_FILE: ".github/steps/1-create-a-branch.md"`

**Permissions Required**:
- `contents: write` - Update README
- `actions: write` - Disable/enable workflows  
- `issues: write` - Create issue and comment

**Example Usage**:
```bash
# Workflow triggers automatically when repository is created from template
git push origin main
```

### 2. Create Branch Workflow

**File**: `.github/workflows/1-create-a-branch.yml`

**Trigger**: Push to branch `my-first-branch`

**Purpose**: Validates that user has successfully created the required branch.

```yaml
name: Step 1 # Create a branch
on:
  push:
    branches:
      - "my-first-branch"
```

**Key Functions**:
- `find_exercise`: Locates the tutorial issue
- `check_step_work`: Validates branch creation
- `post_next_step_content`: Posts step 2 instructions

**Validation Criteria**:
- Branch name must be exactly `my-first-branch`
- Branch must be pushed to GitHub

### 3. Commit File Workflow

**File**: `.github/workflows/2-commit-a-file.yml`

**Trigger**: Push to `my-first-branch` branch

**Purpose**: Validates that user has created and committed the PROFILE.md file.

```yaml
name: Step 2 # Commit a file
on:
  push:
    branches:
      - "my-first-branch"
```

**Key Functions**:
- Checks for existence of `PROFILE.md` file
- Validates file content and location
- Advances to step 3 upon success

**Validation Criteria**:
- File must be named `PROFILE.md`
- File must be in repository root
- File must contain content

### 4. Open Pull Request Workflow

**File**: `.github/workflows/3-open-a-pull-request.yml`

**Trigger**: Pull request events (opened, synchronize, reopened, edited)

**Purpose**: Validates pull request creation and content.

```yaml
name: Step 3 # Open a pull request
on:
  pull_request:
    branches:
      - main
    types:
      - opened
      - synchronize
      - reopened
      - edited
```

**Key Functions**:
- Validates pull request title and description
- Checks source and target branches
- Provides feedback via PR comments

**Validation Criteria**:
- Pull request must target `main` branch
- Source branch should be `my-first-branch`
- Must have title and description

### 5. Merge Pull Request Workflow

**File**: `.github/workflows/4-merge-your-pull-request.yml`

**Trigger**: Push to `main` branch (when PR is merged)

**Purpose**: Completes the tutorial and provides final feedback.

```yaml
name: Step 4 # Merge your pull request
on:
  push:
    branches:
      - main
```

**Key Functions**:
- Validates successful merge
- Posts completion message
- Provides next steps and resources

## Tutorial Steps API

### Step Content Structure

Each tutorial step follows a consistent markdown structure:

```markdown
## Step X: [Title]

_[Motivational message]_

[Learning content and explanations]

### :keyboard: Activity: [Activity name]

[Step-by-step instructions]

<details>
<summary>Having trouble? 🤷</summary><br/>
[Troubleshooting tips]
</details>
```

### Step 1: Create a Branch

**File**: `.github/steps/1-create-a-branch.md`

**Learning Objectives**:
- Understanding repositories and branches
- Creating a new branch in GitHub UI

**Key Concepts Taught**:
- Git and GitHub fundamentals
- Repository structure
- Branch concept and purpose
- Profile README introduction

**Required Actions**:
1. Navigate to Code tab
2. Click main branch dropdown
3. Create branch named `my-first-branch`

### Step 2: Commit a File

**File**: `.github/steps/2-commit-a-file.md`

**Learning Objectives**:
- Understanding commits
- Creating files in GitHub UI
- Writing commit messages

**Key Concepts Taught**:
- What is a commit
- Markdown file basics (.md extension)
- File creation workflow

**Required Actions**:
1. Ensure on `my-first-branch`
2. Create file named `PROFILE.md`
3. Add content: "Welcome to my GitHub profile!"
4. Commit with message "Add PROFILE.md"

### Step 3: Open a Pull Request

**File**: `.github/steps/3-open-a-pull-request.md`

**Learning Objectives**:
- Understanding pull requests
- Collaboration workflows
- Code review process

**Key Concepts Taught**:
- Pull request purpose and benefits
- Comparing branches
- Writing descriptions

**Required Actions**:
1. Open Pull Request from `my-first-branch` to `main`
2. Set title: "Add my first file"
3. Add meaningful description

### Step 4: Merge Pull Request

**File**: `.github/steps/4-merge-your-pull-request.md`

**Learning Objectives**:
- Understanding merges
- Completing the collaboration cycle
- Repository cleanup

**Key Concepts Taught**:
- Merge process and purpose
- Branch cleanup
- Workflow completion

**Required Actions**:
1. Click "Merge pull request"
2. Confirm merge
3. Delete the feature branch

### Review and Next Steps

**File**: `.github/steps/x-review.md`

**Purpose**: Provides completion summary and additional resources.

**Content**:
- Accomplishments recap
- Profile README quick start
- Additional learning resources
- Community engagement links

## Automation Components

### Skills Exercise Toolkit Integration

The tutorial uses the `skills/exercise-toolkit` for common automation tasks:

```yaml
uses: skills/exercise-toolkit/.github/workflows/start-exercise.yml@v0.1.0
uses: skills/exercise-toolkit/.github/workflows/find-exercise-issue.yml@v0.1.0
```

**Key Functions**:
- `start-exercise.yml`: Creates tutorial issues
- `find-exercise-issue.yml`: Locates existing tutorial issues
- Template management for consistent messaging

### Progress Tracking System

**Issue-Based Progress**: Each tutorial uses a GitHub issue for:
- Step-by-step instruction delivery
- Progress tracking and validation
- Real-time feedback and encouragement

**Workflow State Management**: 
- Workflows enable/disable automatically
- Prevents duplicate executions
- Updates status badges dynamically

### Feedback Templates

The system uses markdown templates for consistent messaging:
- `checking-work.md`: Progress validation messages
- `step-finished-prepare-next-step.md`: Completion notifications
- `watching-for-progress.md`: Waiting for user action

## Usage Instructions

### For Learners

#### Starting the Tutorial

1. **Create Repository**: Use the template to create your own copy
   ```bash
   # Repository is created from skills/introduction-to-github template
   ```

2. **Wait for Initialization**: Allow ~20 seconds for setup
   - Watch for issue creation
   - Green "Start Exercise" button activation

3. **Follow Instructions**: Complete each step as outlined in the issue comments

#### Progress Tracking

- **Status Badges**: Check README for step completion status
- **Issue Comments**: Follow real-time feedback in the tutorial issue
- **Workflow Runs**: Monitor Actions tab for validation progress

### For Educators/Administrators

#### Customizing Content

1. **Modify Step Content**: Edit files in `.github/steps/`
   ```markdown
   # Edit .github/steps/1-create-a-branch.md
   # Update learning objectives, instructions, or troubleshooting
   ```

2. **Adjust Validation**: Modify workflow trigger conditions
   ```yaml
   # Example: Change required branch name
   on:
     push:
       branches:
         - "custom-branch-name"
   ```

3. **Update Templates**: Customize feedback messages
   ```yaml
   # Reference custom template files
   env:
     STEP_1_FILE: ".github/steps/custom-step-1.md"
   ```

#### Deployment

1. **Template Repository**: Ensure repository is marked as template
2. **Permissions**: Verify Actions and Issues are enabled
3. **Testing**: Test complete flow with a test repository

## Configuration Reference

### Environment Variables

| Variable | Purpose | Example |
|----------|---------|---------|
| `STEP_1_FILE` | Path to step 1 instructions | `.github/steps/1-create-a-branch.md` |
| `STEP_2_FILE` | Path to step 2 instructions | `.github/steps/2-commit-a-file.md` |
| `STEP_3_FILE` | Path to step 3 instructions | `.github/steps/3-open-a-pull-request.md` |
| `STEP_4_FILE` | Path to step 4 instructions | `.github/steps/4-merge-your-pull-request.md` |
| `ISSUE_URL` | Dynamic issue URL for comments | Set by find-exercise-issue workflow |

### Workflow Permissions

Standard permissions required across workflows:

```yaml
permissions:
  contents: read    # Read repository content
  actions: write    # Enable/disable workflows
  issues: write     # Create and comment on issues
```

Additional permissions for start workflow:
```yaml
permissions:
  contents: write   # Update README and repository files
```

### Trigger Patterns

| Workflow | Trigger Type | Specific Conditions |
|----------|--------------|-------------------|
| Start Exercise | Push | `branches: [main]` |
| Create Branch | Push | `branches: ["my-first-branch"]` |
| Commit File | Push | `branches: ["my-first-branch"]` |
| Open PR | Pull Request | `branches: [main], types: [opened, synchronize, reopened, edited]` |
| Merge PR | Push | `branches: [main]` |

## Examples

### Example 1: Complete Tutorial Flow

```bash
# 1. Create repository from template
# (Done via GitHub UI)

# 2. Wait for start workflow to complete
# Creates issue with step 1 instructions

# 3. Create branch
git checkout -b my-first-branch
git push origin my-first-branch

# 4. Create and commit file
echo "Welcome to my GitHub profile!" > PROFILE.md
git add PROFILE.md
git commit -m "Add PROFILE.md"
git push origin my-first-branch

# 5. Create pull request via GitHub UI
# Set title: "Add my first file"
# Add description of changes

# 6. Merge pull request via GitHub UI
# Complete tutorial and receive final feedback
```

### Example 2: Customizing Step Content

```markdown
<!-- Custom step content example -->
## Step 1: Create Your Feature Branch

_Welcome to our custom GitHub tutorial! 🚀_

**What you'll learn**: In this step, you'll learn how to create a feature branch for your development work.

### :keyboard: Activity: Create a feature branch

1. Navigate to the **Code** tab
2. Click the **main** branch dropdown
3. Enter `feature/my-awesome-feature` as your branch name
4. Click **Create branch**

<details>
<summary>Need help? 🤔</summary><br/>

- Ensure your branch name starts with `feature/`
- Use descriptive names for your branches
- Avoid spaces in branch names

</details>
```

### Example 3: Custom Validation Workflow

```yaml
# Custom workflow for validating specific file patterns
name: Custom Step - Add Configuration

on:
  push:
    branches:
      - "feature/*"

jobs:
  validate_config:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Check for config file
        run: |
          if [ -f "config.json" ]; then
            echo "✅ Configuration file found"
          else
            echo "❌ config.json file is missing"
            exit 1
          fi
      
      - name: Validate JSON syntax
        run: |
          python -m json.tool config.json > /dev/null
          echo "✅ Valid JSON syntax"
```

### Example 4: Multi-Language Support

```yaml
# Workflow supporting multiple programming languages
name: Language-Specific Tutorial

on:
  push:
    paths:
      - '**.py'
      - '**.js'
      - '**.java'

jobs:
  detect_language:
    runs-on: ubuntu-latest
    outputs:
      language: ${{ steps.detect.outputs.language }}
    steps:
      - uses: actions/checkout@v4
      
      - name: Detect programming language
        id: detect
        run: |
          if [ -f "*.py" ]; then
            echo "language=python" >> $GITHUB_OUTPUT
          elif [ -f "*.js" ]; then
            echo "language=javascript" >> $GITHUB_OUTPUT
          elif [ -f "*.java" ]; then
            echo "language=java" >> $GITHUB_OUTPUT
          fi

  provide_feedback:
    needs: detect_language
    runs-on: ubuntu-latest
    steps:
      - name: Language-specific feedback
        run: |
          case "${{ needs.detect_language.outputs.language }}" in
            python)
              echo "Great! You're learning Python with GitHub!"
              ;;
            javascript)
              echo "Excellent! JavaScript and GitHub make a powerful combination!"
              ;;
            java)
              echo "Wonderful! Java development with GitHub is very popular!"
              ;;
          esac
```

## Troubleshooting

### Common Issues

1. **Workflows Not Triggering**
   - Verify branch names match exactly
   - Check workflow permissions
   - Ensure Actions are enabled

2. **Missing Issue Creation**
   - Check repository template status
   - Verify start workflow permissions
   - Wait for workflow completion

3. **Validation Failures**
   - Review step requirements carefully
   - Check file names and locations
   - Verify commit messages

### Debug Steps

1. **Check Workflow Runs**: Navigate to Actions tab
2. **Review Logs**: Examine workflow execution details
3. **Verify Triggers**: Confirm events match workflow conditions
4. **Test Permissions**: Ensure sufficient repository permissions

---

*This documentation covers the complete API surface and usage patterns for the GitHub Skills Introduction to GitHub tutorial. For additional support, visit the [GitHub Skills discussion board](https://github.com/orgs/skills/discussions/categories/introduction-to-github).*