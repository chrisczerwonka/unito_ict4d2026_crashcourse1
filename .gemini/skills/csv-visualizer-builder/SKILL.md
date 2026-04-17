---
name: csv-visualizer-builder
description: Skill for creating and publishing interactive CSV/TSV data visualizers on GitHub Pages with subfolder-based separate URLs. Use when building new map-based data apps that handle geographic CSV uploads.
---

# CSV Visualizer Builder

This skill documents the design, functionality, and publishing process for creating interactive CSV/TSV data visualizers.

## Design & Functionality
The visualizer is a single-page application (SPA) built with:
- **Leaflet.js**: For interactive map rendering.
- **Leaflet.markercluster**: To manage large datasets (thousands of points) by grouping nearby markers.
- **Inter (Google Font)**: For clean, modern typography.
- **Custom CSS**: Scientific Minimalist aesthetic (Teal/Blue primary color).

### Key Features:
1. **Dynamic Upload**: Supports dragging and dropping or pasting CSV/TSV data.
2. **Column Detection**: Automatically identifies latitude, longitude, country, event type, and date columns using common naming patterns.
3. **Data Filtering**: Built-in filters for Country, Event Type, and Date Range.
4. **Side Sidebar & Table**: Synchronized table view with the map; clicking a row zooms to the marker.
5. **Detail Panel**: Displays all columns for a selected record.
6. **Theme Support**: Dark and Light modes with a toggle.

## Usage Workflow

When asked to create a new CSV visualizer:

1. **Prepare the Template**:
   - Use `assets/map-visualizer-template.html` as the base.
   - If the user has specific CSV content (e.g., "Air Quality data"), update the `LABEL_COLUMNS` and other detection patterns in the `<script>` section if necessary.

2. **Publish on GitHub Pages**:
   - Follow the subfolder strategy documented in `references/publishing-workflow.md`.
   - Ensure the new app is in a subfolder like `apps/[new-app-name]/` to maintain a separate URL.
   - The URL will be `https://[username].github.io/[repo-name]/apps/[new-app-name]/`.

3. **Link from Landing Page**:
   - Update the project's root `index.html` to include a new card linking to the newly published application.

## Resources
- **Template**: `assets/map-visualizer-template.html`
- **Publishing Steps**: `references/publishing-workflow.md`
