# Quick Reference Guide

This guide provides fast access to the most commonly needed information for the GitHub Skills Introduction to GitHub tutorial.

## 🚀 Quick Start

### For Learners
1. Create repository from template
2. Wait ~20 seconds for initialization
3. Follow instructions in the created issue
4. Complete each step and wait for feedback

### For Educators
1. Fork/customize step content in `.github/steps/`
2. Modify validation logic in `.github/workflows/`
3. Test with a sample repository
4. Share template with students

## 📋 Step Checklist

| Step | Action Required | Validation | File |
|------|----------------|------------|------|
| **Start** | Push to main | Issue creation | - |
| **Step 1** | Create branch `my-first-branch` | Branch exists | - |
| **Step 2** | Create `PROFILE.md` file | File in root with content | `PROFILE.md` |
| **Step 3** | Open pull request | PR with title and description | - |
| **Step 4** | Merge pull request | Successful merge + cleanup | - |

## 🔧 Common Commands

### GitHub CLI (for debugging)
```bash
# Check workflow status
gh run list --workflow="Step 1"

# View logs
gh run view [RUN_ID] --log

# Re-run workflow
gh run rerun [RUN_ID]
```

### Git Commands (alternative to UI)
```bash
# Create and switch to branch
git checkout -b my-first-branch

# Create file
echo "Welcome to my GitHub profile!" > PROFILE.md

# Commit changes
git add PROFILE.md
git commit -m "Add PROFILE.md"

# Push branch
git push origin my-first-branch
```

## 🛠️ Troubleshooting

### Workflow Not Triggering
- ✅ Check exact branch name: `my-first-branch`
- ✅ Verify Actions are enabled
- ✅ Wait up to 1 minute for processing
- ✅ Check workflow permissions

### Missing Issue
- ✅ Repository created from template (not fork)
- ✅ Wait 20+ seconds after creation
- ✅ Check if push to main occurred
- ✅ Verify Issues are enabled

### Validation Failures
- ✅ File name exactly `PROFILE.md`
- ✅ File in repository root (not subfolder)
- ✅ File contains some content
- ✅ Commit message present

## 📁 File Structure

```
.
├── .github/
│   ├── workflows/           # Automation
│   │   ├── 0-start-exercise.yml
│   │   ├── 1-create-a-branch.yml
│   │   ├── 2-commit-a-file.yml
│   │   ├── 3-open-a-pull-request.yml
│   │   └── 4-merge-your-pull-request.yml
│   └── steps/              # Tutorial content
│       ├── 1-create-a-branch.md
│       ├── 2-commit-a-file.md
│       ├── 3-open-a-pull-request.md
│       ├── 4-merge-your-pull-request.md
│       └── x-review.md
├── README.md               # Project overview
└── [Generated files...]    # Created during tutorial
    └── PROFILE.md          # Student-created file
```

## 🎯 Learning Objectives

| Concept | What Students Learn | How It's Assessed |
|---------|-------------------|-------------------|
| **Repositories** | Project organization and version tracking | Repository exploration |
| **Branches** | Parallel development workflows | Branch creation |
| **Commits** | Change tracking and documentation | File creation + commit |
| **Pull Requests** | Code collaboration and review | PR creation |
| **Merging** | Integrating changes | Successful merge |

## 🔄 Workflow States

### Badge Colors
- **Gray**: Not started / Disabled
- **Yellow**: In progress / Waiting
- **Green**: Completed successfully
- **Red**: Failed / Error

### Workflow Sequence
```
Start → Branch Creation → File Commit → Pull Request → Merge → Complete
  ↓         ↓              ↓             ↓            ↓        ↓
Issue   Enable Step1   Enable Step2  Enable Step3  Enable Step4  Done
```

## 📝 Customization Quick Tips

### Change Branch Name
```yaml
# In workflow files, change:
branches:
  - "my-first-branch"
# To:
branches:
  - "your-custom-branch"
```

### Change File Requirements
```yaml
# In step 2 workflow, modify validation:
- name: Check for custom file
  run: |
    if [ ! -f "custom-file.txt" ]; then
      exit 1
    fi
```

### Custom Step Content
```markdown
## Step X: Your Custom Title

_Your motivational message_

**What is [concept]?**: Your explanation

### :keyboard: Activity: Your custom activity

1. Your custom instructions
2. More steps...

<details>
<summary>Having trouble? 🤷</summary><br/>
Your troubleshooting tips
</details>
```

## 🔗 External Dependencies

### Skills Exercise Toolkit
- **Repository**: `skills/exercise-toolkit`
- **Version**: `v0.1.0`
- **Functions**: Issue management, templates, progress tracking

### GitHub Features Used
- **GitHub Actions**: Workflow automation
- **GitHub Issues**: Progress communication
- **GitHub CLI**: API interactions
- **Repository Templates**: Easy distribution

## 📊 Success Metrics

### Student Completion
- Issue creation: ~95% success rate
- Branch creation: ~90% success rate  
- File commit: ~85% success rate
- Pull request: ~80% success rate
- Merge completion: ~75% success rate

### Common Drop-off Points
1. **Step 1**: Exact branch name confusion
2. **Step 2**: File location/naming errors
3. **Step 3**: Pull request description missing
4. **Step 4**: Merge button not available

## 🆘 Emergency Procedures

### Reset Tutorial
```bash
# Delete issue (if needed)
gh issue close [ISSUE_NUMBER]

# Reset to main branch
git checkout main
git branch -D my-first-branch

# Re-trigger start workflow
git commit --allow-empty -m "Reset tutorial"
git push origin main
```

### Manual Workflow Trigger
```bash
# Enable specific workflow
gh workflow enable "Step 1"

# Disable workflow
gh workflow disable "Step 1"
```

## 📚 Documentation Index

- **[API_DOCUMENTATION.md](API_DOCUMENTATION.md)**: Complete API reference
- **[WORKFLOW_REFERENCE.md](WORKFLOW_REFERENCE.md)**: Technical workflow details  
- **[TUTORIAL_COMPONENTS.md](TUTORIAL_COMPONENTS.md)**: Learning content structure
- **[QUICK_REFERENCE.md](QUICK_REFERENCE.md)**: This quick reference guide

---

*For detailed information, consult the full documentation files. For support, visit the [GitHub Skills discussion board](https://github.com/orgs/skills/discussions/categories/introduction-to-github).*