# Copilot Instructions for Eric's Blog

## Repository Summary

This is a personal blog built with Hugo static site generator, using the Hugo Theme Stack v4. The blog is hosted on GitHub Pages and features content primarily in Chinese (简体中文) covering programming, mathematics, business, and personal learning experiences.

## Tech Stack

- **Hugo**: Static site generator (v0.154.2 in production)
- **Hugo Theme Stack v4**: Theme loaded as a Go module
- **Go**: v1.25.5 (for Hugo modules)
- **Node.js**: v24.12.0 (for dependencies)
- **Dart Sass**: v1.97.1 (for stylesheet compilation)
- **GitHub Pages**: Hosting platform
- **GitHub Actions**: CI/CD for automated deployment and theme updates

## Project Structure

### Key Directories and Files

- **`content/`**: Blog content in Markdown format
  - `content/post/`: Individual blog posts, each in its own directory with `index.md`
  - `content/page/`: Static pages
  - `content/categories/`: Category pages
- **`config/_default/`**: Hugo configuration files split by concern
  - `config.toml`: Main site configuration (baseURL, language settings)
  - `params.toml`: Theme-specific parameters
  - `menu.toml`: Navigation menu configuration
  - `markup.toml`: Markdown rendering settings
  - `module.toml`: Hugo modules configuration
  - `permalinks.toml`: URL structure rules
  - `related.toml`: Related content settings
- **`layouts/`**: Custom Hugo templates that override theme defaults
- **`static/`**: Static assets served as-is
- **`assets/`**: Asset files processed by Hugo (SCSS, images, etc.)
- **`i18n/`**: Internationalization translation files
- **`go.mod`** and **`go.sum`**: Go module files for Hugo theme dependency
- **`.github/workflows/`**: GitHub Actions workflows
  - `deploy.yml`: Build and deploy to GitHub Pages
  - `update-theme.yml`: Daily automatic theme updates

## Build and Development Commands

### Prerequisites

**Required tools:**
- Git
- Go (v1.17 or later)
- Hugo Extended (latest version recommended)
- Dart Sass (for SCSS compilation)
- Node.js (if using npm dependencies)

### Initial Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/ZHAO20060708/ZHAO20060708.github.io.git
   cd ZHAO20060708.github.io
   ```

2. Download Hugo modules (theme):
   ```bash
   hugo mod download
   ```

3. Install Node.js dependencies (if package.json exists):
   ```bash
   npm ci
   ```

### Development Workflow

**Start the development server:**
```bash
hugo server
```
The site will be available at `http://localhost:1313` with live reload enabled.

**Start development server with drafts:**
```bash
hugo server -D
```

**Update the Hugo theme:**
```bash
hugo mod get -u github.com/CaiJimmy/hugo-theme-stack/v4
hugo mod tidy
```

### Build Commands

**Build the site for production:**
```bash
hugo --gc --minify
```
- `--gc`: Run garbage collection after build
- `--minify`: Minify output HTML, CSS, and JS
- Output will be in the `./public` directory

**Build with specific base URL:**
```bash
hugo --gc --minify --baseURL "https://zhao20060708.github.io/"
```

**Clean the public directory:**
```bash
rm -rf public
```

### Testing and Validation

**No automated tests** - This is a static blog with no test suite.

**Manual validation steps:**
1. Run `hugo server` and verify the site loads correctly at `http://localhost:1313`
2. Check that all pages render without errors
3. Verify that images and assets load properly
4. Test navigation menus and links
5. For content changes, preview the specific post/page being modified

**Configuration validation:**
```bash
hugo config
```
This displays the merged configuration from all config files.

**Check for Hugo errors:**
```bash
hugo --verbose
```

## GitHub Actions Workflows

### Deploy Workflow (`.github/workflows/deploy.yml`)

**Triggered by:**
- Push to `main` or `master` branch
- Manual workflow dispatch

**Build process:**
1. Checkout code with full history and submodules
2. Setup Go, Node.js, and Hugo
3. Install Dart Sass
4. Install Node.js dependencies if lock files exist
5. Configure Git for proper character encoding
6. Restore Hugo cache from previous runs
7. Build site with `hugo --gc --minify --baseURL <pages-url> --cacheDir <cache>`
8. Save Hugo cache for next run
9. Upload build artifact
10. Deploy to GitHub Pages

**Expected build time:** 2-5 minutes depending on cache hits

### Update Theme Workflow (`.github/workflows/update-theme.yml`)

**Triggered by:**
- Daily schedule at 00:00 UTC
- Manual workflow dispatch

**Process:**
1. Checkout repository
2. Setup Hugo Extended
3. Run `hugo mod get -u` to update all modules
4. Run `hugo mod tidy` to clean up go.mod and go.sum
5. Auto-commit changes if theme was updated

## Content Guidelines

### Creating a New Post

1. Create a new directory under `content/post/`:
   ```bash
   mkdir content/post/my-new-post
   ```

2. Create `index.md` in that directory with front matter:
   ```markdown
   ---
   title: "My Post Title"
   description: "Post description"
   date: 2024-01-01T00:00:00+00:00
   slug: my-new-post
   categories:
     - Category Name
   tags:
     - tag1
     - tag2
   ---
   
   Your content here...
   ```

3. Add images to the same directory and reference them:
   ```markdown
   ![Alt text](image.jpg)
   ```

### Language and Localization

- Primary language: Chinese (zh-cn)
- CJK language support is enabled (`hasCJKLanguage = true`)
- Translation files in `i18n/` directory
- Default content language set to `zh-cn`

## Common Issues and Solutions

**Issue:** Hugo module not found
**Solution:** Run `hugo mod download` to fetch dependencies

**Issue:** Build fails with SCSS errors
**Solution:** Ensure Dart Sass is installed and in PATH

**Issue:** Git encoding issues with Chinese characters
**Solution:** Run `git config core.quotepath false` (already configured in deploy workflow)

**Issue:** Theme not updating
**Solution:** Run `hugo mod get -u` followed by `hugo mod tidy`

## Important Notes for Code Changes

1. **Character encoding:** The repository uses Chinese content. Always ensure Git is configured with `core.quotepath false` for proper handling.

2. **Hugo modules:** The theme is loaded via Go modules, not git submodules. Use `hugo mod` commands, not `git submodule` commands.

3. **Configuration split:** Hugo configuration is split across multiple files in `config/_default/`. Changes to site settings should be made in the appropriate file (e.g., menu changes go in `menu.toml`, not `config.toml`).

4. **Base URL:** The production base URL is `https://zhao20060708.github.io`. This is configured in `config/_default/config.toml` and overridden during build.

5. **No package.json:** This project may not have npm dependencies. If you need to add them, create a `package.json` first.

6. **Hugo Extended required:** This theme requires Hugo Extended (with SCSS support). Standard Hugo will not work.

7. **Deployment is automatic:** Any push to `main` or `master` branch triggers automatic deployment via GitHub Actions. Test changes locally before pushing.

8. **Theme updates are automatic:** The theme updates daily at 00:00 UTC via GitHub Actions. Manual theme updates should use `hugo mod get -u`.

## Best Practices

- Always test changes locally with `hugo server` before committing
- Keep configuration organized in the split config files
- Use Hugo's content organization (page bundles with index.md)
- Respect the existing Chinese language content and structure
- Follow the established post structure and front matter format
- When modifying workflows, ensure compatibility with GitHub Pages deployment
