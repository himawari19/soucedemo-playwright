# GitHub Actions Workflow Guide

## Overview

This project includes automated GitHub Actions workflows that:
- Run tests automatically on every push and pull request
- Generate HTML test reports
- Publish reports to GitHub Pages
- Comment on pull requests with results

## Workflows

### 1. Test Automation & Publish Report

**File:** `.github/workflows/test-and-publish.yml`

**Triggers:**
- Push to main, master, or develop branches
- Pull requests to main, master, or develop branches
- Daily at midnight UTC

**Steps:**
1. Checkout code
2. Set up Python 3.11
3. Install dependencies
4. Install Playwright browsers
5. Run tests with pytest
6. Generate HTML report
7. Upload report as artifact
8. Deploy to GitHub Pages
9. Comment on PR with results

**Duration:** ~5-10 minutes

### 2. Configure GitHub Pages

**File:** `.github/workflows/pages-config.yml`

**Triggers:**
- After successful test workflow

**Purpose:**
- Ensures GitHub Pages is properly configured
- Sets up deployment settings

## Accessing Reports

### Latest Report
```
https://himawari19.github.io/soucedemo-playwright/reports/report.html
```

### Reports Dashboard
```
https://himawari19.github.io/soucedemo-playwright/
```

### In Pull Requests
When you create a pull request, the workflow will automatically comment with:
- Test summary (passed, failed, skipped)
- Link to full report
- Execution time

## Workflow Status

### Check Status

1. Go to **Actions** tab in GitHub
2. Look for "Test Automation & Publish Report"
3. Click on the workflow run to see details

### View Logs

1. Click on a workflow run
2. Click on "test" job
3. Expand steps to see logs

### Troubleshoot Failures

1. Check the workflow logs for error messages
2. Common issues:
   - Python version mismatch
   - Missing dependencies
   - Playwright browser not installed
   - GitHub Pages not enabled

## Customization

### Change Python Version

Edit `.github/workflows/test-and-publish.yml`:

```yaml
strategy:
  matrix:
    python-version: ['3.11']  # Change version here
```

### Change Test Command

Edit `.github/workflows/test-and-publish.yml`:

```yaml
- name: Run tests
  run: |
    pytest -v --html=reports/report.html --self-contained-html
    # Add more options here
```

### Change Schedule

Edit `.github/workflows/test-and-publish.yml`:

```yaml
schedule:
  - cron: '0 0 * * *'  # Change cron expression
```

Cron examples:
- `0 0 * * *` - Daily at midnight
- `0 */6 * * *` - Every 6 hours
- `0 9 * * MON` - Every Monday at 9 AM
- `0 0 * * 0` - Every Sunday at midnight

### Add More Branches

Edit `.github/workflows/test-and-publish.yml`:

```yaml
on:
  push:
    branches: [ main, master, develop, staging ]
  pull_request:
    branches: [ main, master, develop, staging ]
```

## Environment Variables

To add environment variables to the workflow:

```yaml
env:
  PLAYWRIGHT_BROWSERS_PATH: /ms-playwright
  CI: true
```

## Secrets

To use secrets in the workflow:

1. Go to Settings > Secrets and variables > Actions
2. Click "New repository secret"
3. Add secret name and value
4. Use in workflow: `${{ secrets.SECRET_NAME }}`

Example:
```yaml
- name: Run tests
  env:
    API_KEY: ${{ secrets.API_KEY }}
  run: pytest -v
```

## Artifacts

Test reports are saved as artifacts for 30 days:

1. Go to workflow run
2. Scroll to "Artifacts" section
3. Download `test-report` to get the HTML file

## Notifications

### Email Notifications

GitHub automatically sends emails when:
- Workflow fails
- Workflow succeeds (if configured)

Configure in Settings > Notifications

### Slack Integration

To add Slack notifications:

1. Create Slack webhook
2. Add as repository secret: `SLACK_WEBHOOK`
3. Add step to workflow:

```yaml
- name: Notify Slack
  if: always()
  uses: slackapi/slack-github-action@v1
  with:
    webhook-url: ${{ secrets.SLACK_WEBHOOK }}
    payload: |
      {
        "text": "Test run completed",
        "blocks": [
          {
            "type": "section",
            "text": {
              "type": "mrkdwn",
              "text": "Test Results: ${{ job.status }}"
            }
          }
        ]
      }
```

## Performance

### Optimization Tips

1. **Cache dependencies:**
```yaml
- uses: actions/cache@v3
  with:
    path: ~/.cache/pip
    key: ${{ runner.os }}-pip-${{ hashFiles('**/requirements.txt') }}
```

2. **Parallel jobs:**
```yaml
strategy:
  matrix:
    python-version: ['3.10', '3.11', '3.12']
```

3. **Conditional steps:**
```yaml
- name: Deploy
  if: github.ref == 'refs/heads/main'
  run: # deployment commands
```

## Monitoring

### Workflow Runs

View all workflow runs:
1. Go to **Actions** tab
2. Select workflow
3. See all runs with status

### Metrics

Track over time:
- Average execution time
- Success rate
- Test pass rate

## Troubleshooting

### Workflow Not Running

1. Check if workflow file is in `.github/workflows/`
2. Verify YAML syntax is correct
3. Check branch name matches trigger
4. Ensure workflow is enabled in Actions tab

### Tests Failing in CI

1. Check workflow logs for error messages
2. Run tests locally to reproduce
3. Check for environment-specific issues
4. Verify all dependencies are installed

### Reports Not Publishing

1. Check GitHub Pages is enabled
2. Verify `gh-pages` branch exists
3. Check workflow deployment step
4. Review GitHub Pages settings

### PR Comments Not Appearing

1. Check workflow has permission to comment
2. Verify PR is from same repository
3. Check workflow logs for errors
4. Ensure GitHub token is valid

## Best Practices

1. **Keep workflows simple** - One workflow per purpose
2. **Use meaningful names** - Clear job and step names
3. **Add documentation** - Comment complex steps
4. **Monitor regularly** - Check Actions tab weekly
5. **Update dependencies** - Keep tools current
6. **Test locally first** - Verify before pushing
7. **Use caching** - Speed up workflow runs
8. **Set timeouts** - Prevent hanging jobs

## Resources

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Workflow Syntax](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions)
- [Actions Marketplace](https://github.com/marketplace?type=actions)
- [Playwright CI Guide](https://playwright.dev/python/docs/ci)

---

**Last Updated:** January 1, 2026
