# PESO Project Website

Source for [pesoproject.org](https://pesoproject.org), the public website for the **PESO Project** — a DOE Office of Advanced Scientific Computing Research (ASCR) initiative that stewards, integrates, and advances the scientific software ecosystem, including the [E4S](https://e4s.io) and [Spack](https://spack.io) ecosystems, in coordination with the [Consortium for the Advancement of Scientific Software (CASS)](https://cass.community).

The site is a static [Jekyll](https://jekyllrb.com) site published automatically via [GitHub Pages](https://pages.github.com) from the `main` branch.

## Site structure

- **Home** (`index.html`) — overview and entry points into the rest of the site
- **About** (`about.md` + `about/`) — problem space, project details, and team
- **Thrusts** (`thrusts.md`) — the project's parallel work areas
- **Engage** (`engage.md` + `engage/`) — CASS, BSSw, HPSF, Spack, E4S, and the Frank cluster
- **News** (`news.md` + `news/`) — events and documents
- **Connect** (`connect.md`) — how to get involved or reach the team
- **Genesis Mission** (`genesis-mission.md`) — how PESO supports DOE Genesis Mission teams

Shared layout and content pieces live in:

- `_layouts/` — page templates (`default.html`, `page.html`)
- `_includes/` — reusable partials (nav, header, footer, SEO/analytics, shared copy blocks)
- `_data/` — structured content consumed by templates (e.g. `thrusts.yml`, `news.yml`)
- `assets/` — site CSS
- `images/`, `files/` — images and downloadable documents (reports, posters, slides) referenced from pages

## Local development

### Prerequisites

- Ruby (3.x)
- Jekyll and the plugins used by `_config.yml`:

  ```sh
  gem install jekyll jekyll-sitemap jekyll-feed jekyll-seo-tag
  ```

  (All three plugins are on GitHub Pages' supported-plugins list, so no `Gemfile`/Bundler setup is required to build or deploy.)

### Run the site locally

```sh
jekyll serve
```

Then open [http://127.0.0.1:4000](http://127.0.0.1:4000).

### Build only

```sh
jekyll build
```

Output is written to `_site/` (git-ignored).

## Deployment

The site auto-publishes from the `main` branch via GitHub Pages — there is no separate build/deploy step to run manually. The custom domain is configured in `CNAME` (`pesoproject.org`).

Typical workflow for changes:

1. Create a feature branch off `main`.
2. Make changes and verify locally (`jekyll build` / `jekyll serve`).
3. Open a pull request and merge into `main`.
4. GitHub Pages rebuilds and publishes automatically.

## Contributing

Contributions from the computational science and engineering community are welcome — see [CONTRIBUTING.md](CONTRIBUTING.md). Every published page also has a "Report an issue with this page" link in the footer, which opens a new GitHub issue pre-populated with that page's name and URL for convenient, low-friction feedback.

## License

Released under the [MIT License](LICENSE).
