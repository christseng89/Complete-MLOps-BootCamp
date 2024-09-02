# GitHub Actions

### What is GitHub Actions
GitHub Actions is a powerful automation tool provided by GitHub that allows you to create workflows directly within your GitHub repositories. These workflows can be triggered by events like pushes, pull requests, or scheduled times, enabling you to automate tasks such as building, testing, and deploying your code.

### Key Features of GitHub Actions:

1. CI/CD (Continuous Integration/Continuous Deployment):
   - GitHub Actions is widely used for CI/CD pipelines. You can automate the process of building your code, running tests, and deploying your applications when certain events occur, such as a push to a branch or a pull request.

2. Event-Driven Workflows:
   - Workflows in GitHub Actions can be triggered by various events, such as:
     - Pushes to a repository
     - Pull requests
     - Creation of issues or releases
     - Scheduled times (cron jobs)

3. Customizable Workflows:
   - Workflows are defined using YAML files stored in the `.github/workflows` directory of your repository. You can define multiple jobs within a workflow, specify dependencies between jobs, and use various actions available from the GitHub Marketplace or create your own custom actions.

4. Built-in Support for Multiple Languages and Platforms:
   - GitHub Actions supports a wide range of programming languages and platforms, allowing you to run your workflows on different operating systems (Linux, macOS, Windows) and use various programming environments.

5. Integration with GitHub Ecosystem:
   - GitHub Actions integrates seamlessly with the rest of the GitHub ecosystem, including issues, pull requests, and releases. It allows you to automate processes that are tightly coupled with your development workflow on GitHub.

6. Matrix Builds:
   - GitHub Actions supports matrix builds, allowing you to run your workflows across multiple configurations, such as different versions of a language runtime, different operating systems, or various environment variables.

7. Reusable Actions:
   - You can use pre-built actions from the GitHub Actions Marketplace or share your own actions with the community. This promotes reuse and can significantly speed up the development of your workflows.

### Example Use Cases:
- Automated Testing: Automatically run unit tests every time code is pushed to the repository.
- Continuous Deployment: Deploy a web application to a cloud provider whenever new code is merged into the main branch.
- Code Quality Checks: Run linters, security scanners, or other code quality tools as part of your workflow.
- Scheduled Tasks: Perform regular maintenance tasks, such as cleaning up old branches or generating reports on a regular basis.
- GitHub Actions can automatically package each action (or step) in a CI/CD workflow into a Docker container that includes all the necessary code and dependencies. This process is done by GitHub Actions to ensuring that the action runs in an isolated and consistent environment.

Overall, GitHub Actions is a versatile and integral part of modern DevOps practices, making it easier to Automate and Streamline software development processes directly within the GitHub platform.

### Understanding the Workflow in Github Actions
https://docs.github.com/en/actions/writing-workflows/workflow-syntax-for-github-actions

- Workflows are initiated by specific events like Commits Pushed to a GitHub repository or successful completion of another workflow.
- Workflow instructions are stored in YAML format within a workflow file.
- The file outlines commands/scripts to execute, default configurations, and the execution environment.
- Workflows are segmented into 'JOBS', each responsible for executing a sequence of 'STEPS'.
- Steps execute commands and may utilize self-contained units known as 'ACTIONS'.
- Steps run on computational resources called 'RUNNERS', with default settings allowing for Windows or Linux environments.

### Understanding the Key Terms
- EVENTS: Events are defined triggers that start a workflow, such as creating a branch, opening a pull request, or commenting on an issue.
- JOBS: Jobs are tasks that are executed in a workflow when an event is triggered. A workflow can have multiple jobs running in parallel.
- ACTIONS: Actions are used to perform complex tasks that you may import into workflows, such as sending a notification email. You can build your own actions or reuse open-source actions available on the GitHub marketplace.

### Example YAML Workflow

```yaml
name: CI/CD Pipeline

# 1. Events: This section defines the triggers for the workflow
on:
  push:                     # Trigger the workflow when code is pushed
    branches:
      - main                # Only run the workflow when code is pushed to the 'main' branch
  pull_request:             # Also trigger the workflow when a pull request is opened or updated
    branches:
      - main                # Only for pull requests targeting the 'main' branch

# 2. Jobs: This section defines the tasks to be executed
jobs:
  build:                    # Job name is 'build'
    runs-on: ubuntu-latest  # Specify the operating system/environment for this job

    steps:                  # Steps to execute within this job
      - name: Checkout code # 3. Actions: Use the 'checkout' action to pull the latest code
        uses: actions/checkout@v2

      - name: Set up Node.js environment
        uses: actions/setup-node@v2 # Use an action to set up Node.js
        with:
          node-version: '14' # Specify the Node.js version to use

      - name: Install dependencies
        run: npm install       # Install npm dependencies with a shell command

      - name: Run tests
        run: npm test          # Run the test suite using a shell command

      - name: Build application
        run: npm run build     # Build the application using a shell command

  deploy:                     # Another job named 'deploy'
    runs-on: ubuntu-latest     # This job also runs on Ubuntu
    needs: build               # This job depends on the 'build' job being successful

    steps:
      - name: Deploy to AWS S3
        uses: jakejarvis/s3-sync-action@v0.5.1 # Use an action to sync the build to an S3 bucket
        with:
          args: --acl public-read --delete
        env:
          AWS_S3_BUCKET: ${{ secrets.AWS_S3_BUCKET }} # Use secrets for sensitive data
          AWS_ACCESS_KEY_ID: ${{ secrets.AWS_ACCESS_KEY_ID }}
          AWS_SECRET_ACCESS_KEY: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
```

### Explanation of the Terms:

#### 1. Events (`on`)
   - `push:` This event triggers the workflow whenever code is pushed to the specified branches (in this case, the `main` branch).
   - `pull_request:` This event triggers the workflow when a pull request is opened or updated for the specified branches (`main` in this case). This ensures that the CI/CD pipeline runs for both direct pushes and pull requests.

#### 2. Jobs (`jobs`)
   - `build:`
   - `deploy:`

#### 3. Actions (`uses`)

### Additional Details:
- Steps (`steps`): Each job consists of multiple steps, steps within a job are executed sequentially.
    - runs a command (`run`) or 
    - uses an action (`uses`). 
- Secrets (`secrets`): Sensitive info., such as AWS credentials, is stored in GitHub Secrets `${{ secrets.NAME }}`.

### GitHub Actions DEMO
// GitHub CLI
choco install gh

gh auth login
  ...
  ! First copy your one-time code: BC16-A704 # One time code #
  Press Enter to open github.com in your browser...
  ...

gh auth refresh -h github.com -s delete_repo

// Create new repository

md github-actions-demo
cd github-actions-demo

echo "# github-actions-demo" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main

### Create GitHub repository
gh repo create christseng89/github-actions-demo --public --source=. --push
git status

md .github\workflows
git add .github\workflows\github-actions-demo.yaml
git commit -am "Quick Demo on github actions YAML file"
git push

https://github.com/christseng89/github-actions-demo/actions =>
- name: GitHub Actions Demo
- run-name: christseng89 is testing out GitHub Actions
- job: Explorer-GitHub-Actions

// By the GitHub
- Set up job
- Post Check out repository code
- Complete job

### Delete GitHub repository
gh repo delete christseng89/github-actions-demo
