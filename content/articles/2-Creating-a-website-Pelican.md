Title: Creating a Blog on GitHub.io with Python
Date: 2014-07-05
Slug: creating-a-blog-on-GitHub-dot-io-with-Python
Author: Sean Azlin
Category: Programming
Tags: Python, Pelican, CodeFellows
Summary: How to create a blog on GitHub.io with Python using Pelican

##Creating a Blog on GitHub.io with Python
This article walks through the creation and publication of a blog on GitHub.io (aka GitHub Pages) using a Python static site generator called [Pelican](http://blog.getpelican.com/). To walk through this article you'll need some basic Python skills and a GitHub account.

###Why Python?
I'm currently attending an 8-week Python Development Accelerator at [Code Fellows](http://codefellows.org) in Seattle, WA. My professional goal right now is to immerse myself in all things Python and become an expert in the language. Python is excellent for creating web sites with frameworks such as Flask, Pyramid, and Django, so why not use it to make a blog?

###My Goals for my Blog
I had some general goals in mind when picking a blog platform to migrate to. It's well worth your time to take a minute and think through what it is you want out of your blog before getting started. Here were my goals:

* Create a site where I can share professional articles, tutorials, and other musings with the world
* Have that site be easy to setup and maintain
* Make it easy to author posts for the site, **including when I'm offline**, using [Markdown](http://en.wikipedia.org/wiki/Markdown)
* Exercise my Python and web dev skills
* Spend as little money as possible, ideally none :)

###The Key Components
####Hosting: GitHub.io
**Why?** It's free, I can use git both for source control and for publishing articles, and I already spend tons of time on GitHub anyway.
####Platform: Pelican
**Why?** Pelican is a static site generator. A *static* site is one where the site's HTML is stored on disk and doesn't need to be constructed *dynamically* at runtime to service individual requests. Wordpress and Tumblr are examples of dynamic sites because they construct the HTML that you see at runtime based on content that lives in a database. Compared to dynamic sites, static sites can often be faster, more secure, cheaper to host, easier to move/migrate, and entire sites can be version-controlled easily. 

Pelican is also open source, easy to get started with, fairly popular, has an active community of supporters and plugin developers and, of course, is written in Python :) 
####Frontend: Bootstrap
**Why?** Using [Bootstrap](http://getbootstrap.com/) allows me to prop up a great mobile-first frontend for my site with very little effort. It's a great foundation to build on. I won't get into details about Bootstrap in this article but I've provided some links on how to learn more about using Bootstrap with Pelican below. 
####Deployment: Fabric
**Why?** Running the quick start script for Pelican will give you a basic Fabric script for free that is pretty easy to modify and use without much fuss. I talk more about Fabric in step 2 below.
###Step 1: Start a Blog Project
The first thing I do when starting a new project is use [virtualenv](http://virtualenv.readthedocs.org/en/latest/virtualenv.html) and [virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/) to create a dev environment and project folder for my project using virtualenvwrapper's `mkproject` command: 

    :::text
    $ mkproject blog

If you work with Python and you don't know what virtualenv or virtualenvwrapper are then I highly recommend checking them out to streamline your Python development workflow.

###Step 2: Install Pelican and Create your Blog
Before installing Pelican, make sure you're using Python 2.7 for this project. It's the recommended version of Python for Pelican and it's the version I'm using for this tutorial. You should also install [pip](https://pip.pypa.io/en/latest/installing.html) if you haven't done so already.

Let's get this show on the road! Start by installing Pelican using `pip install`:
    
    :::text
    $ pip install pelican

Pelican supports authoring content with reST OOtB but I prefer Markdown myself. If you're like me then go ahead and install Markdown next:
    
    :::text
    $ pip install markdown

Once that completes you can run the following command to create an initial site:

    :::text
    $ pelican-quickstart

You'll then be asked to answer several questions. Here are the answers I give it for my personal site:

    :::text
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

	:::text
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
* The`output` directory is where your site's html, css, etc. will build into. When you build your site the source files in your `content` directory will be built into output files in your `output` directory.  
* `fabfile.py` is a Python script used by [Fabric](http://www.fabfile.org/), a deployment automation tool that we'll be using for this tutorial. We'll use Fabric to build the site after we make edits, to serve the site locally for testing, and eventually to publish our site to GitHub.io
*  `pelicanconf.py` is a configuration file used by Pelican to build the site. We'll play with the settings in this file shortly.

Let's see if we can give this site a first look-over. To do that we need to install Fabric and then use it to build and serve the site locally:

	:::text
    $ pip install fabric
	...
	$ fab build
	...
	$ fab serve
	
Here's what the last two lines look like for me:
	
	:::text
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
	
	:::text
    $ mkdir ./content/articles
	$ mkdir ./content/images
	$ mkdir ./content/pages
	
Note that I created my new folders **in the `content` directory**, not in the `output` directory. AFAIK, you should never need to add content to the `output` directory manually.

At this point, the directory structure of the blog project should look something like this:

	:::text
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
 
Before going and creating a first blog post we should get our `pelicanconf.py` file in working order. Go ahead and open `pelicanconf.py` in your favorite editor and make the following changes:

* Change the `TIMEZONE` setting to be a value that makes sense for you. I'm using "US/Pacific" myself.
* Change the `LINKS` tuple to include only the links that you want to show up on your site (if you want any links)
* Change the `SOCIAL` tuple to include your Twitter, LinkedIn, GitHub, Facebook, and other social links that you want to show up on your page.
* The `articles` and `pages` directories that we created previously will be recognized by Pelican automatically, but the `images` directory will not. To make sure the `images` directory is recognized and automatically copied into the `output` folder whenever we build the site, we need to add the following: `STATIC_PATHS = ['images',]`.

Here's what my updated `pelicanconf.py` looks like. Try creating one with your own links:

	:::Python
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
	LINKS =  (('CodeFellows', 'http://codefellows.org'),)
	
	# Social widget
	SOCIAL = (('Twitter', 'http://twitter.com/SeanAzlin2'),
	          ('LinkedIn', 'http://linkedin.com/in/seanazlin'),
	          ('GitHub', 'http://github.com/sazlin'),)
	
	STATIC_PATHS = ['images', ]
	
	DEFAULT_PAGINATION = False
	
	# Uncomment following line if you want document-relative URLs when developing
	#RELATIVE_URLS = True

You can learn more about Pelican's settings [here](http://pelican.readthedocs.org/en/3.3.0/settings.html#basic-settings).

Ok, now let's create a simple post to prove this whole thing works. In your terminal:
	
	:::text
    $ touch ./content/articles/first_post.md

Open the file you just created in your favorite editor and copy the following into it:

	:::text
	Title: My First Blog Post
	Date: 2014-7-05 17:20
	Category: MyCategory
	Tags: Tag1, Tag2
	Slug: first-post
	Author: Your Name
	Summary: This is a my first blog post here.
	
	This is a bunch of awesome content that I've written for my post!

Note that Pelican expects and supports the definition of lots of metadata at the beginning of your articles. You can learn more about authoring content on Pelican [here](http://docs.getpelican.com/en/3.3.0/getting_started.html#writing-content-using-pelican).

Save that post and, in your terminal, rebuild the blog and take another look at it in your browser:

	:::text
    $ fab rebuild
	$ fab serve

Your blog should now show a first blog post front and center. You should also see that your category "MyCategory" is shown in the navbar, and your tags are shown on the right. Pelican will automatically group your articles by the categories and tags you set for them and make those available in various parts of the blog's UI. Awesome!

On the bottom you should also see some social icons and some links that reflect what you set in your `pelicanconf.py` file.

Congrats! You now have a simple Pelican blog that you can expand on in a whole bunch of ways. Actually, now's a good time to take a minute and create a git repo for your blog. Let's do that now.

Create a repo on GitHub with a .gitignore file for Python. Call it "blog-repo" or something similar. **NOTE THAT THIS IS NOT THE REPO THAT GITHUB.IO WILL USE**. This is a repo for your blog's source and config files only. You'll create a second repo for GitHub.io later.

Copy the new repo's clone URL and go back into your terminal at the root directory for your project. Run the following commands in-order to add your project to the repo.

	:::text
    $ fab clean
	$ git init
	$ git remote add origin <your repo url>
	$ git pull origin master

The first command, `fab clean`, removes all of the output files (which we don't want in our project's repo since we'll be tracking them in our GitHub.io repo later). The last command, `git pull origin master`, gets the README file and .gitignore file that GitHub created for us. In your favorite editor, open the .gitignore file and add the following entries to it and save:

	cache/
	output/

Ok, now run the following commands back in your terminal:

	:::text
    $ git add .
	$ git commit -m 'Adding blog project files to repo'
	$ git push origin master

Now your blog source and project files are safe in your GitHub repo. Next step: Deploy to GitHub.io.

###Step 3: Deploy to GitHub.io with Fabric
This part is a little bit tricky. One mistake I made early on was thinking that I could use a single GitHub repo for my entire project *and* for GitHub.io. This doesn't work, even if you start with the GitHub.io repo. So, **learn from my mistake and use two repos: one for your project and source files, and one for the output you actually want GitHub.io to host for you**. You already created the repo for your source and project above so now we'll create the repo that GitHub.io will use.

To create a GitHub.io repo, go to GitHub and create a repo that has the following repo name: `<YOUR USERNAME>.github.io`. For example: my GitHub username is 'sazlin' so my GitHub repo is called [sazlin.github.io](https://github.com/sazlin/sazlin.github.io). **Getting the name of this repo correct is critical! GitHub.io will not pick up your Pelican site if the name of the repo doesn't match that schema.** Once you've created your `username.github.io` repo, copy the GitHub URL for it and return to your terminal. **DO NOT continue with the directions on the github.io homepage**. You'll see why in a second.

Ok, back in your terminal you're going to want to install [ghp-import](https://github.com/davisp/ghp-import). This tool make it a little bit easier to put the right content into the right branch for GitHub.io. Here are the commands you want to run through to publish your content to GitHub.io for the first time!

	:::text
    $ pip install ghp-import
	...
	$ pelican content -o output -s pelicanconf.py
	$ ghp-import output
	$ git push <your <username>.github.io repo URL> gh-pages:master

That's it! You've just pushed your blog's output to GitHub.io. Within about 10 minutes you should be able to go to `http://<your username>.github.io` and see your simple Pelican blog published for all the world to see.

The last thing that you should probably do now is automate the last set of commands you just ran for whenever you want to update your blog on GitHub.io. Open your `fabfile.py` file and create a method like this one:

	:::Python
    def publish():
    	local('pelican content -o output -s pelicanconf.py')
    	local('ghp-import output')
    	local('git push https://github.com/sazlin/sazlin.github.io.git gh-pages:master')
    	
Now if you ever have a new article or page to publish you can push it up by running:

	:::text
    $ fab publish

Last, but not least, be sure to commit your latest source and project settings to your blog's project repo:

	:::text
    $ fab clean
	$ git add .
	$ git commit -m "Added publish() to fabfile.py for deploying to GitHub.io"
	$ git push origin master

###What's Next?
You're on your way! Next you might want to peruse some other great articles and documentation about Pelican. Here are a couple resources and plugins I found useful:

* [Official Pelican Docs](http://pelican.readthedocs.org/en/3.3.0/): These docs are actually pretty good and are well worth bookmarking for when you have questions about configuring or using Pelican.
* [Creating you blog with Pelican](http://chdoig.github.io/create-pelican-blog.html): This article by Christine Doig has some great info about how to change up the look and feel of your blog.
* [pelican-bootstrap3](https://github.com/DandyDev/pelican-bootstrap3): This Pelican theme enables you to use Bootstrap with your Pelican site.
* [pelican-plugins](https://github.com/getpelican/pelican-plugins): A collection of Pelican plugins, some of which you might want to use. I recommend `liquid_tags.img`.
* [Bootswatch](http://bootswatch.com/): A great collection of free Bootstrap themes.
* [Disqus](https://disqus.com/websites/): If you want comments for your articles then check out Disqus. I haven't used it personally but I've heard good things about it.