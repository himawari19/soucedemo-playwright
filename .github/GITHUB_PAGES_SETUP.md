# GitHub Pages Setup Guide

This guide explains how to set up and use GitHub Pages for publishing test reports.

## Automatic Setup

The GitHub Actions workflow automatically:
1. Runs tests on every push and pull request
2. Generates HTML test reports
3. Publishes reports to GitHub Pages
4. Creates a reports dashboard

## Manual Setup (if needed)

### Step 1: Enable GitHub Pages

1. Go to your repository on GitHub
2. Click **Settings** (gear icon)
3. Scroll down to **Pages** section
4. Under "Build and deployment":
   - Source: Select "Deploy from a branch"
   - Branch: Select "gh-pages"
   - Folder: Select "/ (root)"
5. Click **Save**

### Step 2: Verify Workflow

1. Go to **Actions** tab
2. Look for "Test Automation & Publish Report" workflow
3. Check that it runs successfully
4. The workflow will create the `gh-pages` branch automatically

### Step 3: Access Published Reports

Once the workflow completes:
- **Latest Report:** https://himawari19.github.io/soucedemo-playwright/reports/report.html
- **Dashboard:** https://himawari19.github.io/soucedemo-playwright/

## Workflow Details

### Triggers

The workflow runs on:
- Every push to main, master, or develop branches
- Every pull request to main, master, or develop branches
- Daily at midnight (UTC)

### What It Does

1. **Checks out code** - Gets the latest repository code
2. **Sets up Python** - Installs Python 3.11
3. **Installs dependencies** - Runs `pip install -r requirements.txt`
4. **Installs Playwright** - Sets up Chromium browser
5. **Runs tests** - Executes all 37 test cases
6. **Generates report** - Creates HTML test report
7. **Publishes to GitHub Pages** - Deploys report to gh-pages branch
8. **Comments on PR** - Adds test results to pull requests

### Report Structure

```
gh-pages branch/
├── index.html              # Reports dashboard
├── reports/
│   ├── report.html         # Latest test report
│   └── [run-number]/       # Historical reports
│       └── report.html
```

## Accessing Reports

### Latest Report
Direct link to the most recent test report:
```
https://himawari19.github.io/soucedemo-playwright/reports/report.html
```

### Reports Dashboard
Overview of all test reports:
```
https://himawari19.github.io/soucedemo-playwright/
```

### Historical Reports
Each workflow run creates a timestamped report:
```
https://himawari19.github.io/soucedemo-playwright/reports/[run-number]/report.html
```

## Customization

### Change Report Location

Edit `.github/workflows/test-and-publish.yml`:

```yaml
- name: Deploy to GitHub Pages
  uses: peaceiris/actions-gh-pages@v3
  with:
    github_token: ${{ secrets.GITHUB_TOKEN }}
    publish_dir: ./reports          # Change this path
    destination_dir: reports        # Change destination
```

### Change Workflow Schedule

Edit the cron schedule in `.github/workflows/test-and-publish.yml`:

```yaml
schedule:
  - cron: '0 0 * * *'  # Daily at midnight UTC
  # Other examples:
  # - cron: '0 */6 * * *'  # Every 6 hours
  # - cron: '0 9 * * MON'  # Every Monday at 9 AM
```

### Add More Branches

Edit the workflow triggers:

```yaml
on:
  push:
    branches: [ main, master, develop, staging ]  # Add branches
  pull_request:
    branches: [ main, master, develop, staging ]
```

## Troubleshooting

### Reports Not Publishing

1. Check workflow status in **Actions** tab
2. Look for error messages in workflow logs
3. Verify GitHub Pages is enabled in Settings
4. Ensure `gh-pages` branch exists

### GitHub Pages Not Updating

1. Wait a few minutes for deployment to complete
2. Hard refresh browser (Ctrl+Shift+R or Cmd+Shift+R)
3. Check GitHub Pages deployment status in Settings > Pages
4. Verify workflow completed successfully

### Workflow Failing

1. Check workflow logs for error messages
2. Verify Python version compatibility
3. Ensure all dependencies are in requirements.txt
4. Check Playwright browser installation

## Security

### Secrets

The workflow uses `${{ secrets.GITHUB_TOKEN }}` which is automatically provided by GitHub Actions. No additional secrets need to be configured.

### Permissions

The workflow requires:
- `contents: read` - To read repository code
- `pages: write` - To publish to GitHub Pages
- `id-token: write` - For OIDC token generation

These are automatically configured in the workflow file.

## Best Practices

1. **Keep reports organized** - Historical reports are kept for reference
2. **Monitor workflow status** - Check Actions tab regularly
3. **Review test results** - Check reports after each run
4. **Update documentation** - Keep README.md with latest report links
5. **Archive old reports** - Periodically clean up old reports if needed

## Additional Resources

- [GitHub Pages Documentation](https://docs.github.com/en/pages)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Playwright Documentation](https://playwright.dev/python/)
- [Pytest Documentation](https://docs.pytest.org/)

## Support

For issues or questions:
1. Check GitHub Actions logs
2. Review workflow file syntax
3. Verify GitHub Pages settings
4. Check repository permissions

---

**Last Updated:** January 1, 2026
