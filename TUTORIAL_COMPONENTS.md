# Tutorial Components Reference

This document provides comprehensive documentation for all tutorial components, learning content, and step-by-step instructions in the GitHub Skills Introduction to GitHub exercise.

## Component Architecture

The tutorial uses a modular component system with:
- **Step Files**: Markdown-based learning content
- **Workflow Validators**: Automated progress checking
- **Feedback System**: Real-time user guidance
- **Progress Tracking**: Issue-based communication

## Learning Content Components

### Step 1: Create a Branch (1-create-a-branch.md)

#### Component Structure
```markdown
## Step 1: Create a branch

_Welcome to "Introduction to GitHub"! :wave:_

[Educational content]

### :keyboard: Activity: Your first branch

[Step-by-step instructions]

<details>
<summary>Having trouble? 🤷</summary><br/>
[Troubleshooting section]
</details>
```

#### Learning Objectives
| Objective | Description | Assessment Method |
|-----------|-------------|-------------------|
| **Git Concepts** | Understanding Git vs GitHub | Conceptual explanation |
| **Repository Structure** | Learning about repositories | Interactive exploration |
| **Branching Fundamentals** | Creating and using branches | Hands-on branch creation |
| **Profile README** | Introduction to GitHub profiles | Contextual explanation |

#### Educational Content Blocks

##### 1. Platform Introduction
```markdown
**What is GitHub?**: GitHub is a collaboration platform that uses _[Git](https://docs.github.com/get-started/quickstart/github-glossary#git)_ for versioning.
GitHub is a popular place to share and contribute to [open-source](https://docs.github.com/get-started/quickstart/github-glossary#open-source) software.

:tv: [Video: What is GitHub?](https://www.youtube.com/watch?v=pBy1zgt0XPc)
```

**Purpose**: Establishes foundational understanding of GitHub's role in software development.

**Learning Strategy**: 
- Video reinforcement for visual learners
- Glossary links for detailed definitions
- Real-world context (open-source)

##### 2. Repository Concepts
```markdown
**What is a repository?**: A _[repository](https://docs.github.com/get-started/quickstart/github-glossary#repository)_ is a project containing files and folders.
A repository tracks versions of files and folders.
```

**Purpose**: Introduces version control fundamentals.

**Key Concepts**:
- File and folder organization
- Version tracking mechanism
- Project containerization

##### 3. Branching Theory
```markdown
**What is a branch?**: A _[branch](https://docs.github.com/en/get-started/quickstart/github-glossary#branch)_ is a parallel version of your repository.
By default, your repository has one branch named `main` and it is considered to be the definitive branch.
```

**Purpose**: Explains parallel development workflows.

**Core Principles**:
- Parallel development capability
- Main branch as source of truth
- Safe experimentation environment

#### Interactive Activity Component

##### Activity Structure
```markdown
### :keyboard: Activity: Your first branch

1. Open a new browser tab and navigate to your newly made repository
2. Navigate to the **< > Code** tab in the header menu
3. Click on the **main** branch drop-down
4. In the text box **Find or create a branch...**, enter `my-first-branch`
5. Click the text **Create branch: `my-first-branch` from main**
6. Wait for workflow validation and feedback
```

**Design Principles**:
- Clear step numbering for easy following
- Specific UI element targeting
- Expected outcomes described
- Validation feedback integration

##### Visual Aids Integration
- Screenshots for complex UI interactions
- Annotated images highlighting specific elements
- Progressive visual flow matching steps

#### Troubleshooting Component
```markdown
<details>
<summary>Having trouble? 🤷</summary><br/>

If you don't get feedback, here are some things to check:
- Make sure your created the branch with the exact name `my-first-branch`
- No prefixes or suffixes

</details>
```

**Features**:
- Collapsible design to reduce visual clutter
- Common error scenarios addressed
- Specific validation criteria clarified

---

### Step 2: Commit a File (2-commit-a-file.md)

#### Component Structure
Advanced step building on branch creation knowledge.

#### Learning Objectives
| Objective | Description | Validation Criteria |
|-----------|-------------|-------------------|
| **Commit Concepts** | Understanding commits as change sets | File creation and commit |
| **File Creation** | GitHub UI file operations | PROFILE.md existence |
| **Commit Messages** | Writing descriptive commit messages | Specific message format |
| **Markdown Basics** | Introduction to .md files | File extension usage |

#### Educational Content Blocks

##### 1. Commit Theory
```markdown
**What is a commit?**: A _[commit](https://docs.github.com/pull-requests/committing-changes-to-your-project/creating-and-editing-commits/about-commits)_ is a set of changes to the files and folders in your project.
A commit exists in a branch.
```

**Key Concepts**:
- Change set atomic operations
- Branch-specific commits
- Project history building blocks

##### 2. Markdown Introduction
```markdown
> [!NOTE]
> `.md` is a file extension that creates a Markdown file. You can learn more about Markdown by visiting "[Basic writing and formatting syntax](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)"
```

**Educational Strategy**:
- Just-in-time learning approach
- External resource references
- Future learning pathway suggestions

#### Interactive Activity Component

##### File Creation Workflow
```markdown
1. On the **< > Code** tab, make sure you're on your new branch `my-first-branch`
2. Select the **Add file** drop-down and click **Create new file**
3. In the **Name your file...** field, enter `PROFILE.md`
4. In the **Enter file contents here** area, copy the following content:
   ```
   Welcome to my GitHub profile!
   ```
5. Click **Commit changes...** in the upper right corner
6. Enter `Add PROFILE.md` in the **Commit message** field
7. Click **Commit changes**
```

**Design Features**:
- Branch context validation
- Specific file naming requirements
- Exact content specification
- Commit message guidance

##### Progressive Complexity
- Builds on previous branch knowledge
- Introduces file operations
- Adds commit message concepts
- Maintains validation integration

---

### Step 3: Open a Pull Request (3-open-a-pull-request.md)

#### Component Structure
Collaboration-focused step introducing peer review concepts.

#### Learning Objectives
| Objective | Description | Assessment |
|-----------|-------------|------------|
| **Pull Request Concepts** | Understanding collaborative workflows | PR creation |
| **Code Review Basics** | Introduction to review processes | Title and description |
| **Branch Comparison** | Understanding change visualization | Branch selection |
| **Communication Skills** | Writing descriptive PR descriptions | Content quality |

#### Educational Content Blocks

##### 1. Collaboration Theory
```markdown
**What is a pull request?**: Collaboration happens on a _[pull request](https://docs.github.com/en/get-started/quickstart/github-glossary#pull-request)_.
The pull request shows the changes in your branch to other people and allows people to accept, reject, or suggest additional changes to your branch.
```

**Core Concepts**:
- Collaborative change proposal
- Change visualization and review
- Accept/reject/suggest workflow
- Side-by-side comparison view

#### Interactive Activity Component

##### Pull Request Creation Workflow
```markdown
1. In the header menu of your repository, click the **Pull requests** tab
2. Click the **New pull request** button
3. Select the following branches using the dropdown menus:
   - **base:** `main`
   - **compare:** `my-first-branch`
4. Click **Create pull request**
5. Enter a title: `Add my first file`
6. Add a meaningful description of changes
7. Click **Create pull request**
```

**Advanced Features**:
- Multiple pathway options (automatic vs manual)
- Branch relationship understanding
- Title and description requirements
- Real-world communication skills

##### Alternative Workflow Support
```markdown
You may have noticed after your commit that a message displayed indicating your recent push to your branch and providing a button that says **Compare & pull request**.

To create a pull request automatically, click **Compare & pull request** button, and then skip to step 5 below.
```

**Adaptive Learning**:
- Recognizes different user paths
- Provides shortcut instructions
- Maintains learning objective alignment

---

### Step 4: Merge Pull Request (4-merge-your-pull-request.md)

#### Component Structure
Final integration step completing the collaborative cycle.

#### Learning Objectives
| Objective | Description | Completion Criteria |
|-----------|-------------|-------------------|
| **Merge Concepts** | Understanding code integration | Successful merge |
| **Workflow Completion** | Completing collaborative cycles | Branch cleanup |
| **Repository Maintenance** | Branch lifecycle management | Branch deletion |
| **Success Recognition** | Celebrating achievements | Tutorial completion |

#### Educational Content Blocks

##### 1. Merge Theory
```markdown
**What is a merge?**: A _[merge](https://docs.github.com/en/get-started/quickstart/github-glossary#merge)_ adds the changes in your pull request and branch into the `main` branch.
```

**Key Concepts**:
- Change integration process
- Main branch update mechanism
- Permanent change incorporation

#### Interactive Activity Component

##### Merge Workflow
```markdown
1. Click **Merge pull request**
2. Click **Confirm merge**
3. Once your branch has been merged, you don't need it anymore
4. To delete this branch, click **Delete branch**
```

**Workflow Features**:
- Two-step confirmation process
- Branch lifecycle completion
- Repository cleanup education

##### Advanced Concepts
```markdown
> **Tip:** Did you notice this dialog looks similar to adding a file? A merge is also a kind of commit!
```

**Educational Connections**:
- Links new concepts to previous learning
- Reinforces underlying Git principles
- Builds conceptual understanding

---

### Review and Completion (x-review.md)

#### Component Structure
Comprehensive completion summary and next steps guidance.

#### Content Blocks

##### 1. Achievement Summary
```markdown
Here's a recap of your accomplishments:
- You learned about GitHub, repositories, branches, commits, and pull requests
- You created a branch, a commit, and a pull request
- You merged a pull request
- You made your first contribution! :tada:
```

**Purpose**: Reinforces learning achievements and builds confidence.

##### 2. Next Steps Guidance
```markdown
### What's next?

If you'd like to make a profile README, use the quickstart instructions below:

1. Make a new public repository with a name that matches your GitHub username
2. Create a file named `README.md` in its root
3. Edit the contents of the `README.md` file
4. If you created a new branch for your file, open and merge a pull request
5. We'd love to hear what you thought of this exercise [in our discussion board](https://github.com/orgs/skills/discussions/categories/introduction-to-github)
```

**Features**:
- Practical next steps
- Real-world application
- Community engagement
- Feedback collection

##### 3. Resource Extension
```markdown
Check out these resources to learn more or get involved:
- Are you a student? Check out the [Student Developer Pack](https://education.github.com/pack)
- [Take another GitHub Skills exercise](https://skills.github.com)
- [Read the GitHub Getting Started docs](https://docs.github.com/en/get-started)
- To find projects to contribute to, check out [GitHub Explore](https://github.com/explore)
```

**Learning Pathway**:
- Audience-specific resources
- Progressive skill building
- Official documentation
- Community contribution opportunities

## Component Design Patterns

### 1. Progressive Disclosure
- Information revealed as needed
- Building complexity gradually
- Context-appropriate detail levels

### 2. Multi-Modal Learning
- Text explanations
- Visual aids (screenshots)
- Video resources
- Interactive activities

### 3. Validation Integration
- Real-time feedback
- Automated progress checking
- Clear success criteria
- Error handling guidance

### 4. Accessibility Features
- Clear heading hierarchy
- Descriptive link text
- Alt text for images
- Keyboard navigation support

### 5. Motivational Design
- Encouraging language
- Progress celebration
- Achievement recognition
- Community connection

## Customization Guidelines

### Content Adaptation
```markdown
## Step X: [Custom Title]

_[Custom motivational message]_

**What is [concept]?**: [Custom explanation with relevant links]

### :keyboard: Activity: [Custom activity name]

[Custom step-by-step instructions]

<details>
<summary>Having trouble? 🤷</summary><br/>
[Custom troubleshooting guidance]
</details>
```

### Validation Criteria Modification
- Update workflow trigger conditions
- Modify file name requirements
- Adjust content validation rules
- Customize feedback messages

### Learning Objective Alignment
- Map activities to specific skills
- Ensure assessment validity
- Maintain progression logic
- Validate educational outcomes

---

*This component reference provides the educational and structural foundation for understanding and customizing the GitHub Skills tutorial content system.*