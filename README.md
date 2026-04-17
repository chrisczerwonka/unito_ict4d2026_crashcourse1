# FloodKit: Bangladesh Flood Analytics & Risk Mapping

This project is an open-data platform for visualizing climate resilience in Bangladesh, focusing on historical flood trends and critical infrastructure vulnerability.

## Project Structure

- **`index.html`**: The main landing page.
- **`apps/`**: Interactive web applications.
  - `flood-risk/`: Map-based visualization of priority districts and flood incidence.
  - `flood-analytics/`: Charts and trends of historical flood data.
  - `map-visualizer/`: A generic tool for mapping any CSV/TSV geographic data.
- **`data/`**: Cleaned datasets in CSV, GeoJSON, and XLSX formats.
- **`tools/`**: Development tools and templates, including the `csv-visualizer-builder` skill.
- **`scripts/`**: Data processing and conversion scripts.

## Features

- **Spatial Analysis**: Interactive maps highlighting high-risk zones and infrastructure.
- **Trend Dashboards**: Time-series analysis of over 5,000 global flood events.
- **Custom Mapping**: Drag-and-drop CSV visualization tool.

## Technical Stack

- **Frontend**: Vanilla HTML/CSS/JS, Leaflet.js, Chart.js.
- **Data Parsing**: PapaParse, Openpyxl (Python).
- **Styling**: Inter Google Font, Scientific Minimalist aesthetic.

## How to View

The project is designed to be hosted on GitHub Pages. The main entry point is `index.html`.
