# Deployment Checklist

Follow these steps to deploy the test automation suite with GitHub Pages reporting.

## Pre-Deployment

- [ ] All tests pass locally: `pytest -v`
- [ ] README.md is updated with GitHub Pages links
- [ ] GitHub Actions workflows are in `.github/workflows/`
- [ ] Repository is on GitHub
- [ ] You have admin access to the repository

## Step 1: Push Code to GitHub

```bash
# Add all files
git add .

# Commit changes
git commit -m "Add test automation with GitHub Actions and Pages"

# Push to main branch
git push origin main
```

- [ ] Code pushed successfully
- [ ] No merge conflicts
- [ ] All files committed

## Step 2: Enable GitHub Pages

1. Go to your repository on GitHub
2. Click **Settings** (gear icon)
3. Scroll down to **Pages** section
4. Under "Build and deployment":
   - [ ] Source: Select "Deploy from a branch"
   - [ ] Branch: Select "gh-pages"
   - [ ] Folder: Select "/ (root)"
5. Click **Save**

- [ ] GitHub Pages enabled
- [ ] gh-pages branch selected
- [ ] Root folder selected

## Step 3: Verify Workflow

1. Go to **Actions** tab
2. Look for "Test Automation & Publish Report" workflow
3. Wait for workflow to complete (5-10 minutes)

- [ ] Workflow started automatically
- [ ] All steps completed successfully
- [ ] No errors in logs

## Step 4: Verify GitHub Pages Deployment

1. Go to **Settings** > **Pages**
2. Look for deployment status
3. Should show "Your site is live at: https://himawari19.github.io/soucedemo-playwright/"

- [ ] GitHub Pages deployment successful
- [ ] Site is live
- [ ] URL is accessible

## Step 5: Access Published Reports

### Latest Report
```
https://himawari19.github.io/soucedemo-playwright/reports/report.html
```

### Reports Dashboard
```
https://himawari19.github.io/soucedemo-playwright/
```

- [ ] Latest report accessible
- [ ] Dashboard accessible
- [ ] Report displays correctly

## Step 6: Test Pull Request Integration

1. Create a new branch: `git checkout -b test-pr`
2. Make a small change
3. Push branch: `git push origin test-pr`
4. Create a pull request on GitHub
5. Wait for workflow to complete

- [ ] Workflow runs on PR
- [ ] PR comment appears with test results
- [ ] Report link in PR comment works

## Step 7: Verify Scheduled Runs

The workflow is configured to run daily at midnight UTC.

- [ ] Check Actions tab tomorrow
- [ ] Verify daily run completed
- [ ] Check report was updated

## Post-Deployment

### Update Documentation

- [ ] README.md has GitHub Pages links
- [ ] Links point to correct URLs
- [ ] CI/CD section is complete

### Monitor Workflow

- [ ] Check Actions tab regularly
- [ ] Review test results
- [ ] Monitor for failures

### Share Links

Share these links with your team:

**Latest Report:**
```
https://himawari19.github.io/soucedemo-playwright/reports/report.html
```

**Reports Dashboard:**
```
https://himawari19.github.io/soucedemo-playwright/
```

**Repository:**
```
https://github.com/himawari19/soucedemo-playwright
```

## Troubleshooting

### Workflow Not Running

1. Check if workflow file exists: `.github/workflows/test-and-publish.yml`
2. Verify YAML syntax is correct
3. Check branch name matches trigger (main/master/develop)
4. Enable workflow in Actions tab if disabled

### Reports Not Publishing

1. Check GitHub Pages is enabled in Settings
2. Verify `gh-pages` branch exists
3. Check workflow deployment step in logs
4. Review GitHub Pages settings

### PR Comments Not Appearing

1. Check workflow has permission to comment
2. Verify PR is from same repository
3. Check workflow logs for errors
4. Ensure GitHub token is valid

### Site Not Accessible

1. Wait a few minutes for deployment
2. Hard refresh browser (Ctrl+Shift+R)
3. Check GitHub Pages deployment status
4. Verify custom domain settings (if applicable)

## Maintenance

### Regular Tasks

- [ ] Monitor workflow runs weekly
- [ ] Review test results
- [ ] Update dependencies monthly
- [ ] Archive old reports quarterly

### Customization

- [ ] Adjust workflow schedule if needed
- [ ] Add more branches to triggers
- [ ] Customize report dashboard
- [ ] Add Slack notifications

### Backup

- [ ] Backup workflow files
- [ ] Document any customizations
- [ ] Keep README.md updated

## Success Criteria

✅ All items checked means successful deployment:

- [ ] Code pushed to GitHub
- [ ] GitHub Pages enabled
- [ ] Workflow runs successfully
- [ ] Reports published to GitHub Pages
- [ ] PR comments working
- [ ] Documentation updated
- [ ] Team notified with links

## Support

For issues or questions:

1. Check `.github/GITHUB_PAGES_SETUP.md`
2. Check `.github/WORKFLOW_GUIDE.md`
3. Review GitHub Actions logs
4. Check GitHub Pages settings

## Next Steps

After successful deployment:

1. Share report links with team
2. Monitor workflow runs
3. Update CI/CD as needed
4. Add more test cases
5. Integrate with other tools (Slack, etc.)

---

**Deployment Date:** _______________

**Deployed By:** _______________

**Notes:** _______________________________________________

---

**Last Updated:** January 1, 2026
