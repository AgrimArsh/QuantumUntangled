<img align="right" width="60" height="60" src="media/logo.png" alt="Quantum Untangled logo icon">

# Quantum Untangled
This is the `gh-pages` branch of the Quantum Untangled website repository. This version of our publication is hosted with [GitHub pages](https://pages.github.com) and developed using Jekyll. To start development of this website, the [Millennial](https://github.com/LeNPaul/Millennial#configuration) free Jekyll theme was used, but several modifications have been made to the theme and more modifications will be made to personalize our website. 

## Setting up
To start, clone this repo into your local machine and run `git switch gh-pages` to pull this branch from this remote repository and checkout to it. Once you are in this branch, you have two options:

- If you just want to publish an article(s), you don't need to install anything else and you can follow the instructions on the following section.
- If you want to contribute to the development of the webiste, follow the instructions on the last section in this document to install the requirements. 

## Publish an article
To publish an article to this website, open an issue first talking about your article idea and make sure to go through the already published articles so you don't talk about a topic already covered. 

We will discuss your intended article with you and you will submit a draft in Markdown format. Remember that Jekyll uses kramdown to parse posts, therefore LaTeX is supported (it must be encolsed by double dollar signs e.g. `$$ x^2 + 1 $$`) in addition to the standard Markdown syntax. To submit your draft, you need to add the document to the `_posts` directory and add the following to the top of your file:

```
---
layout: post
title: "{title of your post}"
author: "{your name}"
categories: {category; discussed beforehand in your issue}
tags: [{tags separated by a comma; discussed beforehand in your issue}]
image: {name of the image you want as cover of your post}
---
```

Then, you can submit a pull request (linked to your issue) and the post will be reviewed. Changes will be discussed if needed and finally the post will be merged into the branch. 

## Develop the website
To work in the development of this website, you need to first install Ruby and Jekyll so you're able to run the webiste locally. To install Ruby, go to https://www.ruby-lang.org and follow the instructions corresponding to your system. Then, run the following commands in your command line:

```
gem update
gem install jekyll bundler
```

Now, you can run the website on your local machine by running the following:

```
bundler exec jekyll serve
```

The link to the website will show up on the terminal and any changes you make to the website will be shown in real time. To push any changes you make to the project, open a pull request to discuss what you worked on so we can agree on how to proceed. 
