Title: Creating a Blog with Python
Date: 2014-07-03
Slug: creating-a-blog-with-Python
Author: Sean Azlin
Category: Programming
Summary: How to use Python to create a free personal blog & website

##Creating a Blog on GitHub.io with Python
This article walks walks through the creation and publication of a blog on github.io. To walk through it you'll need some basic Python skills and a GitHub account.

###Why Python?
I'm currently attending an 8-week Python Development Accelerator at Code Fellows in Seattle, WA. My professional goal right now is to immerse myself in all things Python and become an expert in the language. Python is excellent for creating web sites with frameworks such as Flask, Pyramid, and Django, so why not use it to make a blog?

###My goals for my blog
I had some general goals in mind when picking a blog platform to migrate to. It's well worth your time to take a minute and think through what it is you want out of your blog before getting started. Here were my goals:
 
* Create a site where I can share professional articles, tutorials, and other musings with the world
* Have that site be easy to setup and maintain
* Make it easy to author posts for the site, **including when I'm offline**, using Markdown
* Exercise my Python and web dev skills
* Spend as little money as possible, ideally none :)

###The key components
####Hosting: GitHub.io
**Why?** It's free, I can use git both for source control and for publishing articles, and I already spend tons of time on GitHub anyway.
####Platform: Pelican
**Why?** Pelican is a static site generator. It's open source, fairly popular, has an active community of supporters and plugin developers and, of course, it's written in Python :) Using a static site generator is great for me because my site's experience isn't going to include any self-hosted dynamic elements like comment streams or authoring & editing UI for my articles. This negates the need for a dynamic blog engine like Wordpress.
####Frontend: Bootstrap
**Why?** Using Bootstrap allows me to prop up a great mobile-first frontend for my site with very little effort. It's a great foundation to build on.
####Deployment: Fabric
**Why?** Running the quick start script for Pelican will give you a Fabric script for free that is pretty easy to modify and use without much fuss. I talk more about Fabric in step 2 below.
###Step 1: Start a Blog Project
The first thing I do when starting a new project is use [virtualenv](http://virtualenv.readthedocs.org/en/latest/virtualenv.html) and [virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/) to create a new environment and project folder for my project using virtualenvwrapper's `mkproject` command: 

    $ mkproject blog

If you work with Python and you don't know what virtualenv or virtualenvwrapper are then I highly recommend checking them out to streamline your dev workflow.

###Step 2: Install Pelican
Before installing Pelican, make sure you're using Python 2.7 for this project. It's the recommended version of Python for Pelican and it's the version I'm using for this tutorial.

Now, install Pelican using `pip install`:
    
    $ pip install pelican

Pelican supports authoring content with reST OOtB, but I prefer Markdown myself. So next I will also install Markdown:
    
    $ pip install markdown

Once that completes you can run the following command to create your initial site:

    $ pelican-quickstart

You'll then be asked to answer several questions. Here are the answers I give it for my personal site:

    seans-mbp:blog sazlin$ pelican-quickstart
	Welcome to pelican-quickstart v3.4.0.

	This script will help you create a new Pelican-based website.

	Please answer the following questions so this script can generate the files
	needed by Pelican.

	Using project associated with current virtual environment.Will save to:
    /Users/sazlin/projects/blog
    
    > What will be the title of this web site? Sean Azlin's Blog
    > Who will be the author of this web site? Sean Azlin
    > What will be the default language of this web site? [en] en
    > Do you want to specify a URL prefix? e.g., http://example.com   (Y/n) n
    > Do you want to enable article pagination? (Y/n) n
    > Do you want to generate a Fabfile/Makefile to automate generation and publishing? (Y/n) Y
    > Do you want an auto-reload & simpleHTTP script to assist with theme and site development? (Y/n) Y
    > Do you want to upload your website using FTP? (y/N) N
    > Do you want to upload your website using SSH? (y/N) N
    > Do you want to upload your website using Dropbox? (y/N) N
    > Do you want to upload your website using S3? (y/N) N
    > Do you want to upload your website using Rackspace Cloud Files? (y/N) N
    > Do you want to upload your website using GitHub Pages? (y/N) Y
    > Is this your personal page (username.github.io)? (y/N) Y
    Done. Your new project is available at /Users/sazlin/projects/blog

Afterwards, your project's directory should look something like this:

	.
	├── Makefile
	├── content
	├── develop_server.sh
	├── fabfile.py
	├── output
	├── pelicanconf.py
	└── publishconf.py

So what's all this? 

* The `content` directory is essentially where the source files for your site live. The source for your articles will live there in addition to any resources, such as images, that you include in your articles.
* The`output` directory is where your site's html, css, etc. will live and be served out of. When you build your site the source files in your `content` directory will be built into output files in your `output` directory.  
* `fabfile.py` is a Python script used by Fabric, a deployment automation tool that we'll be using for this tutorial. We'll use Fabric to build the site after we make edits, to serve the site locally for testing, and eventually to publish our site to GitHub.io
*  pelicanconf.py is a configuration file used by Pelican to build the site. We'll play with the settings in this file shortly.

Let's see if we can give this site a first look-over. To do that we need to install Fabric and then use it to build and serve the site locally:

	$ pip install fabric
	...
	$ fab build
	...
	$ fab serve
	
Here's what the last two lines look like for me:
	
	seans-mbp:blog sazlin$ fab build
	[localhost] local: pelican -s pelicanconf.py
	WARNING: Feeds generated without SITEURL set properly may not be valid
	WARNING: No valid files found in content.
	Done: Processed 0 article(s), 0 draft(s) and 0 page(s) in 0.10 seconds.

	Done.
	[blog]
	seans-mbp:blog sazlin$ fab serve
	Serving on port 8000 ...

Ignore the warnings for now. Open up your favorite browser and browse to `localhost:8000`. You should see a fairly simple blog with your name on it.

If you take a minute to look over your site's directory structure then you'll see that there's a lot more stuff in it now, especially in your `output` directory. Now you can see all the HTML, CSS, and images that Pelican builds for your site. 

Ok, so here's a question: Where is *your* content going to live in that output directory? In my case, I want to have my articles live in their own folder and my images live in their own folder. I also want a folder for my site's pages that aren't articles, such as my "About Me" page. To accomplish this, I'm going to ctrl+c in my terminal and create a few directories:
	
	$ mkdir ./content/articles
	$ mkdir ./content/images
	$ mkdir ./content/pages
	
Note that I created my new folders **in the `content` directory**, not in the `output` directory. AFAIK, you should never need to add content to the `output` directory manually.

At this point, the directory structure of the blog project should look something like this:

	.
	├── Makefile
	├── blog.sublime-project
	├── cache
	│   ├── ArticlesGenerator-Readers
	│   └── PagesGenerator-Readers
	├── content
	│   ├── articles
	│   └── images
	│   └── pages
	├── develop_server.sh
	├── fabfile.py
	├── fabfile.pyc
	├── output
	│   ├── archives.html
	│   ├── authors.html
	│   ├── categories.html
	│   ├── index.html
	│   ├── tags.html
	│   └── theme
	│       ├── css
	│       │   ├── main.css
	│       │   ├── pygment.css
	│       │   ├── reset.css
	│       │   ├── typogrify.css
	│       │   └── wide.css
	│       └── images
	│           └── icons
	│               ├── aboutme.png
	│               ├── bitbucket.png
	│               ├── delicious.png
	│               ├── facebook.png
	│               ├── github.png
	│               ├── gitorious.png
	│               ├── gittip.png
	│               ├── google-groups.png
	│               ├── google-plus.png
	│               ├── hackernews.png
	│               ├── lastfm.png
	│               ├── linkedin.png
	│               ├── reddit.png
	│               ├── rss.png
	│               ├── slideshare.png
	│               ├── speakerdeck.png
	│               ├── stackoverflow.png
	│               ├── twitter.png
	│               ├── vimeo.png
	│               └── youtube.png
	├── pelicanconf.py
	├── pelicanconf.pyc
	└── publishconf.py
 
Before going and creating a first blog post we should get our `pelicanconf.py` file in working order. Go ahead and open `pelicanconf.py` in your favorite editor and making the following changes:

* Change `TIMEZONE` setting to be a value that makes sense for you. I'm using "US/Pacific" myself.
* Change the `LINKS` tuple to include only the links that you want to show up on your site (if you want any links)
* Change the `SOCIAL` tuple to include your Twitter, LinkedIn, GitHub, Facebook, and other social links that you want to show up on your page.
* The `articles` and `pages` directories that we created previously will be recognized by Pelican automatically, but the `images` directory will not. To make sure the `images` directory is recognized and automatically copied into the `output` folder whenever we build the site, we need to add the following: `STATIC_PATHS = ['images',]`.

Here's what my updated `pelicanconf.py` looks like:

	#!/usr/bin/env python
	# -*- coding: utf-8 -*- #
	from __future__ import unicode_literals
	
	AUTHOR = u'Sean Azlin'
	SITENAME = u"Sean Azlin's Blog"
	SITEURL = ''
	
	PATH = 'content'
	
	TIMEZONE = 'US/Pacific'
	
	DEFAULT_LANG = u'en'
	
	# Feed generation is usually not desired when developing
	FEED_ALL_ATOM = None
	CATEGORY_FEED_ATOM = None
	TRANSLATION_FEED_ATOM = None
	
	# Blogroll
	LINKS =  (('rheTOracle', 'http://ec2-54-213-173-105.us-west-2.compute.amazonaws.com/'),)
	
	# Social widget
	SOCIAL = (('Twitter', 'http://twitter.com/SeanAzlin2'),
	          ('LinkedIn', 'http://linkedin.com/in/seanazlin'),
	          ('GitHub', 'http://github.com/sazlin'),)
	
	STATIC_PATHS = ['images', ]
	
	DEFAULT_PAGINATION = False
	
	# Uncomment following line if you want document-relative URLs when developing
	#RELATIVE_URLS = True

Ok, now let's create a simple post to prove this whole thing works. In your terminal:
	
	$ touch ./content/articles/first_post.md

Open the file you just created in your favorite editor and copy the following into it:

 

###Step 3: Deploy to GitHub.io with Fabric
###Step 4: Publish your First Article
###Step 5: Install Bootstrap
###Step 6: Pick a Bootstrap Theme you like
###Step 7: Install Pelican-Plugins
###Step 8: Install the plugins that you need
####Commenting
Since this article is talking about creating a *blog* with Pelican, it's worth pointing out that having comments for my blog posts are a non-goal for me. If I wanted comments I'd probably look to a service like [Disqus](https://disqus.com/websites/) to assist with that since static site generators don't really have a good story for comments OOtB.
###Gotchas to watch out for
###Sources and Inspirations
Here are some additional sites to check out for more information and perspectives on creating a blog with Pelican:

* [Creating your blog with Pelican](http://chdoig.github.io/create-pelican-blog.html) (great article by Christine Doig)
* asd 