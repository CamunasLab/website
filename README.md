# Camunas-Soler Lab Website

Welcome to the web page of the **Camunas-Soler lab**. This guide will help you navigate the Hugo codebase, add new content, and update existing pages.

## Table of Contents

1. [Getting Started](#getting-started)
2. [Project Structure](#project-structure)
3. [Adding Content](#adding-content)
4. [Updating Pages](#updating-pages)
5. [Customizing the Homepage](#customizing-the-homepage)
6. [Contact Information](#contact-information)

## Getting Started

### Prerequisites

- [Hugo](https://gohugo.io/getting-started/installing/) (version 0.80.0 or later)
- Git

### Installation

1. Clone the repository:

    ```sh
    git clone <link from website repository>
    cd website
    ```

2. Run the Hugo server:

    ```sh
    hugo server -D 
    ```

    This will start a local development server at `http://localhost:1313`.
    Note: `hugo -h` will give you an overview of available commands and options.

## Project Structure

The main files and directories you will work with are:

- `config/_default/`: Configuration files for the Hugo site.
- `content/`: Directory containing markdown files for different sections of the site.
- `layouts/`: Custom layout templates.
- `static/`: Static files like images, CSS, and JavaScript.
- `assets/`: SCSS and other asset files.

When you run `hugo server`, these directories will also be generated:

- `public/`: Generated files by Hugo (should not be edited directly).
- `resources/`: Automatically generated files by Hugo.

### Directory Overview

- **`config/_default/`**: Contains configuration files (e.g., `hugo.yaml`, `menus.yaml`, `params.yaml`) to set up site-wide settings.
- **`content/`**: Contains the content of your site. Each subdirectory represents a different section.
  - **`_index.md`**: Main homepage content.
  - **`about/`**: About page content.
  - **`admin/`**: Administration content.
  - **`authors/`**: Author profiles.
  - **`contact/`**: Contact page content.
  - **`img/`**: Images used in content.
  - **`people/`**: Team members.
  - **`posts/`**: Blog posts.
  - **`protocols/`**: Protocols and methods.
  - **`publication/`**: Publications.
- **`layouts/`**: Custom templates for different content types.
  - **`_default/`**: Default layout templates.
  - **`section/`**: Templates for sections (e.g., protocols section).
  - **`shortcodes/`**: Custom shortcodes.
- **`static/`**: Static files served as-is (e.g., `static/images` for images).
- **`assets/`**: Source files for stylesheets and JavaScript.
- **`public/`**: The output directory for generated site files.
- **`resources/`**: Processed files used by Hugo.

## Adding Content

### Adding News Posts

To add a new post:

1. Create a new markdown file in the `content/posts/` directory:

    ```sh
    touch content/posts/my-new-post.md
    ```

2. Edit the file and add the following front matter and content:

    ```markdown
    ---
    title: "My New Post"
    date: 2024-08-07
    draft: true
    tags: 
        - talk
    featureimage: "/path/to/feature-image.jpg"
    type: post
    ---

    Content of the news post goes here.
    ```

    Set `draft: false` to publish the post. Use the `tags` field to categorize the news post, e.g., `tags: ["event"]`.

### Adding Protocols

To add a new protocol:

1. Create a new markdown file in the `content/protocols/` directory:

    ```sh
    touch content/protocols/my-new-protocol.md
    ```

2. Edit the file and add the following front matter and content:

    ```markdown
    ---
    title: "My New Protocol"
    date: 2024-08-07
    draft: true
    tags: 
        - protocol
    type: protocol
    ---

    Detailed steps of the protocol go here.
    ```

## Updating Pages

To update an existing page, simply edit the corresponding markdown file in the `content/` directory. For example, to update the "About Us" page, edit `content/about/index.md`.

### Example of Editing the About Page

```markdown
---
title: "About Us"
date: 2024-08-07
---

Updated content for the About Us page goes here.
