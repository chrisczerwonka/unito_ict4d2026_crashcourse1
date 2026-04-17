# Publishing Workflow for CSV Visualizers

To publish a new CSV visualizer web app on GitHub Pages with a separate URL, follow this subfolder-based strategy:

## 1. Directory Structure
Always organize the project using subfolders to keep applications isolated.
- Root: `index.html` (Landing page)
- New App: `apps/[app-name]/index.html` (Copy of the visualizer template)

## 2. Git Commands
Assuming you are on the `main` branch:

```bash
# Create the subfolder
mkdir -p apps/[app-name]

# Copy the template
cp [path-to-template] apps/[app-name]/index.html

# (Optional) Update relative paths in the new index.html if it links to root assets (like styles.css)

# Stage and commit
git add apps/[app-name]/index.html
git commit -m "Add new [app-name] CSV visualizer"

# Push to main
git push origin main
```

## 3. GitHub Pages URL
Once pushed, the application will be available at:
`https://[username].github.io/[repo-name]/apps/[app-name]/`

This ensures it is separate from the main project landing page and other applications.
