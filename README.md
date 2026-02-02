# Eric's Blog

[![Deploy to Github Pages](https://github.com/ZHAO20060708/ZHAO20060708.github.io/actions/workflows/deploy.yml/badge.svg)](https://github.com/ZHAO20060708/ZHAO20060708.github.io/actions/workflows/deploy.yml)

Welcome to Eric Zhao's personal blog! This site is built with [Hugo](https://gohugo.io/) using the [Hugo theme Stack](https://github.com/CaiJimmy/hugo-theme-stack).

## About This Blog

This is a personal blog by Eric Zhao (赵), a double-degree university student from Changchun. The blog primarily features content in Chinese (简体中文) covering:

- **Programming & Computer Science** - C language tutorials, programming concepts, and technical notes
- **Mathematics** - Mathematical concepts, problem-solving, and learning notes  
- **Business & Management** - Studies in business and management theory
- **Personal Learning Journey** - Experiences and insights from university studies

The blog runs on EndeavourOS (Arch Linux-based) and content is updated on a random schedule (随缘更新).

## Visit the Blog

🌐 **Live Site**: [https://zhao20060708.github.io](https://zhao20060708.github.io)

## Technical Details

This blog is built using:
- **Hugo** - Static site generator
- **Hugo Theme Stack v4** - A beautiful and feature-rich Hugo theme
- **GitHub Pages** - Hosting platform
- **GitHub Actions** - Automated deployment and theme updates

### Automatic Deployment

The site automatically deploys to GitHub Pages when changes are pushed to the `master` branch. The deployment workflow:
1. Builds the site using Hugo with optimized caching
2. Deploys directly to GitHub Pages using the native deployment action
3. Updates are live within minutes

### Automatic Theme Updates

The Hugo theme is automatically updated daily via a scheduled GitHub Action to ensure the latest features and security updates.

## Development

### Local Development Setup

If you want to run this blog locally for development:

**Prerequisites**: You need Git, Go, and Hugo extended installed locally.

1. Clone the repository:
   ```bash
   git clone https://github.com/ZHAO20060708/ZHAO20060708.github.io.git
   cd ZHAO20060708.github.io
   ```

2. Install Hugo modules:
   ```bash
   hugo mod download
   ```

3. Run the development server:
   ```bash
   hugo server
   ```

4. Open your browser to `http://localhost:1313`

### Updating the Theme

To manually update the Hugo theme:

```bash
hugo mod get -u github.com/CaiJimmy/hugo-theme-stack/v4
hugo mod tidy
```

> **Note**: This site is now configured with `v4` of the theme. The theme is automatically updated daily via GitHub Actions to ensure the latest features and security updates.

## Contributing

Feel free to open issues or submit pull requests if you find any problems or have suggestions for improvements.

## License

This project is licensed under the terms specified in the [LICENSE](LICENSE) file.

---

*Built with ❤️ using Hugo and deployed on GitHub Pages*
