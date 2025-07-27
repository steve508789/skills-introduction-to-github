# GitHub Actions Workflow Reference

This document provides detailed technical specifications for all GitHub Actions workflows in the Introduction to GitHub Skills exercise.

## Workflow Architecture

The tutorial system uses a sequential workflow architecture where each workflow:
1. Validates specific user actions
2. Provides immediate feedback
3. Enables the next workflow in the sequence
4. Disables itself to prevent re-execution

## Workflow Specifications

### 0-start-exercise.yml

**Purpose**: Initialize the tutorial environment and create the first learning issue.

#### Triggers
```yaml
on:
  push:
    branches:
      - main
```

#### Jobs

##### `start_exercise`
- **Type**: Reusable workflow call
- **Source**: `skills/exercise-toolkit/.github/workflows/start-exercise.yml@v0.1.0`
- **Condition**: `!github.event.repository.is_template`
- **Parameters**:
  - `exercise-title`: "Introduction to GitHub"
  - `intro-message`: Welcome message about issues and collaboration

##### `post_next_step_content`
- **Dependencies**: `[start_exercise]`
- **Environment**: `ISSUE_URL: ${{ needs.start_exercise.outputs.issue-url }}`
- **Steps**:
  1. **Checkout**: Standard repository checkout
  2. **Get response templates**: Clone exercise-toolkit for templates
  3. **Create comment - add step content**: Post step 1 instructions
  4. **Create comment - watching for progress**: Add progress monitoring message
  5. **Disable current workflow and enable next one**: Workflow state management

#### Environment Variables
- `STEP_1_FILE`: `.github/steps/1-create-a-branch.md`

#### Outputs
- `issue-url`: URL of the created tutorial issue

---

### 1-create-a-branch.yml

**Purpose**: Validate branch creation and advance to file commit step.

#### Triggers
```yaml
on:
  push:
    branches:
      - "my-first-branch"
```

#### Jobs

##### `find_exercise`
- **Type**: Reusable workflow call
- **Source**: `skills/exercise-toolkit/.github/workflows/find-exercise-issue.yml@v0.1.0`
- **Purpose**: Locate the existing tutorial issue

##### `check_step_work`
- **Dependencies**: `find_exercise`
- **Runner**: `ubuntu-latest`
- **Environment**: `ISSUE_URL: ${{ needs.find_exercise.outputs.issue-url }}`
- **Steps**:
  1. **Get response templates**: Clone exercise-toolkit
  2. **Update comment - checking work**: Update issue with validation status
  3. **Build message - step finished**: Generate completion message
  4. **Update comment - step finished**: Post completion notification

##### `post_next_step_content`
- **Dependencies**: `[find_exercise, check_step_work]`
- **Steps**:
  1. **Checkout**: Repository checkout
  2. **Get response templates**: Clone exercise-toolkit
  3. **Create comment - add step content**: Post step 2 instructions
  4. **Create comment - watching for progress**: Add monitoring message
  5. **Disable current workflow and enable next one**: Enable step 2 workflow

#### Environment Variables
- `STEP_2_FILE`: `.github/steps/2-commit-a-file.md`

#### Validation Logic
- Branch name must exactly match `my-first-branch`
- Branch must be successfully pushed to remote

---

### 2-commit-a-file.yml

**Purpose**: Validate file creation and commit, then advance to pull request step.

#### Triggers
```yaml
on:
  push:
    branches:
      - "my-first-branch"
```

#### Jobs Structure
Similar to 1-create-a-branch.yml with these key differences:

##### Validation Logic
- Checks for existence of `PROFILE.md` file in repository root
- Validates file contains content
- Confirms commit was made to correct branch

##### Environment Variables
- `STEP_3_FILE`: `.github/steps/3-open-a-pull-request.md`

##### Workflow Progression
- Disables "Step 2" workflow
- Enables "Step 3" workflow

---

### 3-open-a-pull-request.yml

**Purpose**: Validate pull request creation and content.

#### Triggers
```yaml
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

#### Advanced Features

##### Multi-Event Handling
Unlike previous workflows, this handles multiple PR events:
- **opened**: Initial PR creation
- **synchronize**: New commits pushed to PR branch
- **reopened**: PR reopened after being closed
- **edited**: PR title or description modified

##### Validation Components
1. **Pull Request Metadata**:
   - Title validation (must be meaningful)
   - Description validation (must be present)
   - Branch validation (source: `my-first-branch`, target: `main`)

2. **Content Validation**:
   - Confirms PR contains the PROFILE.md file
   - Validates PR shows expected changes

##### Environment Variables
- `STEP_4_FILE`: `.github/steps/4-merge-your-pull-request.md`

---

### 4-merge-your-pull-request.yml

**Purpose**: Complete the tutorial upon successful merge.

#### Triggers
```yaml
on:
  push:
    branches:
      - main
```

#### Completion Logic

##### Merge Detection
- Triggers when commits are pushed to main branch
- Validates that push resulted from PR merge
- Confirms tutorial file is now in main branch

##### Final Steps
1. **Completion Validation**: Verify all tutorial steps completed
2. **Final Feedback**: Post congratulatory message and next steps
3. **Resource Sharing**: Provide links to additional learning materials
4. **Cleanup**: Disable all tutorial workflows

## Common Workflow Patterns

### Error Handling
All workflows include error handling for:
- Missing permissions
- Network failures
- Template file errors
- GitHub API rate limits

### Security Considerations
- Minimal permission sets (`contents: read`, `actions: write`, `issues: write`)
- No secret exposure in logs
- Template repository validation
- User input sanitization

### Performance Optimization
- Conditional job execution
- Minimal checkout operations
- Efficient template caching
- Parallel step execution where possible

## Integration Points

### Skills Exercise Toolkit
All workflows integrate with the external toolkit:
- **Version**: `v0.1.0`
- **Repository**: `skills/exercise-toolkit`
- **Key Functions**:
  - Issue management
  - Template processing
  - Progress tracking
  - Feedback generation

### GitHub API Usage
Workflows extensively use the GitHub CLI (`gh`) for:
- Issue commenting
- Workflow management
- Repository operations
- Status updates

## Debugging Workflows

### Common Debug Commands
```bash
# Check workflow status
gh run list --workflow="Step 1"

# View workflow logs
gh run view [RUN_ID] --log

# Re-run failed workflow
gh run rerun [RUN_ID]

# Check workflow file syntax
gh workflow view "Step 1"
```

### Log Analysis
Key log sections to examine:
- **Trigger validation**: Confirms workflow should run
- **Permission checks**: Validates required permissions
- **Template processing**: Confirms template files loaded
- **API calls**: Shows GitHub API interactions
- **Conditional logic**: Shows why steps were skipped/executed

## Customization Guide

### Adding New Steps
1. Create new step file in `.github/steps/`
2. Create corresponding workflow in `.github/workflows/`
3. Update environment variables for file references
4. Modify workflow enable/disable sequences

### Modifying Validation Logic
```yaml
# Example: Custom file validation
- name: Validate custom requirements
  run: |
    if [ ! -f "custom-file.txt" ]; then
      echo "❌ Custom file missing"
      exit 1
    fi
    
    if ! grep -q "expected-content" "custom-file.txt"; then
      echo "❌ File content validation failed"
      exit 1
    fi
    
    echo "✅ All validations passed"
```

### Custom Feedback Templates
```yaml
# Reference custom template
- name: Post custom feedback
  run: |
    gh issue comment "$ISSUE_URL" \
      --body-file .github/templates/custom-feedback.md
  env:
    GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

## Monitoring and Analytics

### Workflow Metrics
- Execution frequency
- Success/failure rates
- Average execution time
- User completion rates

### Badge Integration
Status badges in README automatically update based on workflow states:
- Gray: Workflow disabled/not started
- Green: Workflow completed successfully
- Red: Workflow failed
- Yellow: Workflow in progress

---

*This workflow reference provides the technical foundation for understanding, debugging, and customizing the GitHub Skills tutorial automation system.*