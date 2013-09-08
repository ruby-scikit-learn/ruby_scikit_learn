


<!DOCTYPE html>
<html>
  <head prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/fb# githubog: http://ogp.me/ns/fb/githubog#">
    <meta charset='utf-8'>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <title>ruby_scikit_learn/scikit-example/digit_classification.py at master · andreas-hjortgaard/ruby_scikit_learn</title>
    <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub" />
    <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub" />
    <link rel="apple-touch-icon" sizes="57x57" href="/apple-touch-icon-114.png" />
    <link rel="apple-touch-icon" sizes="114x114" href="/apple-touch-icon-114.png" />
    <link rel="apple-touch-icon" sizes="72x72" href="/apple-touch-icon-144.png" />
    <link rel="apple-touch-icon" sizes="144x144" href="/apple-touch-icon-144.png" />
    <link rel="logo" type="image/svg" href="https://github-media-downloads.s3.amazonaws.com/github-logo.svg" />
    <meta property="og:image" content="https://github.global.ssl.fastly.net/images/modules/logos_page/Octocat.png">
    <meta name="hostname" content="github-fe119-cp1-prd.iad.github.net">
    <meta name="ruby" content="ruby 1.9.3p194-tcs-github-tcmalloc (2012-05-25, TCS patched 2012-05-27, GitHub v1.0.36) [x86_64-linux]">
    <link rel="assets" href="https://github.global.ssl.fastly.net/">
    <link rel="xhr-socket" href="/_sockets" />
    
    


    <meta name="msapplication-TileImage" content="/windows-tile.png" />
    <meta name="msapplication-TileColor" content="#ffffff" />
    <meta name="selected-link" value="repo_source" data-pjax-transient />
    <meta content="collector.githubapp.com" name="octolytics-host" /><meta content="github" name="octolytics-app-id" /><meta content="432d1eac-7735-4b5b-af0d-cf92eac79c2f" name="octolytics-dimension-request_id" /><meta content="2734140" name="octolytics-actor-id" /><meta content="andreas-hjortgaard" name="octolytics-actor-login" /><meta content="0e3309b7f534729bdecdb459336be63c6caa29c8e08a22962f2b021be5ba90fd" name="octolytics-actor-hash" />
    

    
    
    <link rel="icon" type="image/x-icon" href="/favicon.ico" />

    <meta content="authenticity_token" name="csrf-param" />
<meta content="hUoikWuKrKcXXO8NJ7elQLZNp0Fm3hmCkPpjxF9CpY4=" name="csrf-token" />

    <link href="https://github.global.ssl.fastly.net/assets/github-8d13b140cf7e2873c4dd1e0f589136f0e71bd381.css" media="all" rel="stylesheet" type="text/css" />
    <link href="https://github.global.ssl.fastly.net/assets/github2-d75c750a6b14571dc070b6570d9224acd7b6795e.css" media="all" rel="stylesheet" type="text/css" />
    


      <script src="https://github.global.ssl.fastly.net/assets/frameworks-f86a2975a82dceee28e5afe598d1ebbfd7109d79.js" type="text/javascript"></script>
      <script src="https://github.global.ssl.fastly.net/assets/github-5289a6d6f7dbb5c517007827e10db51fd3ea0251.js" type="text/javascript"></script>
      
      <meta http-equiv="x-pjax-version" content="119d1d5ab0189c49025edd294a6b79f2">

        <link data-pjax-transient rel='permalink' href='/andreas-hjortgaard/ruby_scikit_learn/blob/2ed6b66dde7c0a2bf8155947fbe819372b196949/scikit-example/digit_classification.py'>
  <meta property="og:title" content="ruby_scikit_learn"/>
  <meta property="og:type" content="githubog:gitrepository"/>
  <meta property="og:url" content="https://github.com/andreas-hjortgaard/ruby_scikit_learn"/>
  <meta property="og:image" content="https://github.global.ssl.fastly.net/images/gravatars/gravatar-user-420.png"/>
  <meta property="og:site_name" content="GitHub"/>
  <meta property="og:description" content="ruby_scikit_learn - Ruby Scikit Learn"/>

  <meta name="description" content="ruby_scikit_learn - Ruby Scikit Learn" />

  <meta content="2734140" name="octolytics-dimension-user_id" /><meta content="andreas-hjortgaard" name="octolytics-dimension-user_login" /><meta content="12546664" name="octolytics-dimension-repository_id" /><meta content="andreas-hjortgaard/ruby_scikit_learn" name="octolytics-dimension-repository_nwo" /><meta content="true" name="octolytics-dimension-repository_public" /><meta content="true" name="octolytics-dimension-repository_is_fork" /><meta content="12546581" name="octolytics-dimension-repository_parent_id" /><meta content="ruby-scikit-learn/ruby_scikit_learn" name="octolytics-dimension-repository_parent_nwo" /><meta content="12546581" name="octolytics-dimension-repository_network_root_id" /><meta content="ruby-scikit-learn/ruby_scikit_learn" name="octolytics-dimension-repository_network_root_nwo" />
  <link href="https://github.com/andreas-hjortgaard/ruby_scikit_learn/commits/master.atom" rel="alternate" title="Recent Commits to ruby_scikit_learn:master" type="application/atom+xml" />

  </head>


  <body class="logged_in  env-production macintosh vis-public fork page-blob">
    <div class="wrapper">
      
      
      


      <div class="header header-logged-in true">
  <div class="container clearfix">

    <a class="header-logo-invertocat" href="https://github.com/">
  <span class="mega-octicon octicon-mark-github"></span>
</a>

    <div class="divider-vertical"></div>

    
    <a href="/notifications" class="notification-indicator tooltipped downwards" data-gotokey="n" title="You have unread notifications">
        <span class="mail-status unread"></span>
</a>    <div class="divider-vertical"></div>


      <div class="command-bar js-command-bar  in-repository">
          <form accept-charset="UTF-8" action="/search" class="command-bar-form" id="top_search_form" method="get">

<input type="text" data-hotkey="/ s" name="q" id="js-command-bar-field" placeholder="Search or type a command" tabindex="1" autocapitalize="off"
    
    data-username="andreas-hjortgaard"
      data-repo="andreas-hjortgaard/ruby_scikit_learn"
      data-branch="master"
      data-sha="8058cb1863ef7093715d8a604eab2b3b0df387de"
  >

    <input type="hidden" name="nwo" value="andreas-hjortgaard/ruby_scikit_learn" />

    <div class="select-menu js-menu-container js-select-menu search-context-select-menu">
      <span class="minibutton select-menu-button js-menu-target">
        <span class="js-select-button">This repository</span>
      </span>

      <div class="select-menu-modal-holder js-menu-content js-navigation-container">
        <div class="select-menu-modal">

          <div class="select-menu-item js-navigation-item js-this-repository-navigation-item selected">
            <span class="select-menu-item-icon octicon octicon-check"></span>
            <input type="radio" class="js-search-this-repository" name="search_target" value="repository" checked="checked" />
            <div class="select-menu-item-text js-select-button-text">This repository</div>
          </div> <!-- /.select-menu-item -->

          <div class="select-menu-item js-navigation-item js-all-repositories-navigation-item">
            <span class="select-menu-item-icon octicon octicon-check"></span>
            <input type="radio" name="search_target" value="global" />
            <div class="select-menu-item-text js-select-button-text">All repositories</div>
          </div> <!-- /.select-menu-item -->

        </div>
      </div>
    </div>

  <span class="octicon help tooltipped downwards" title="Show command bar help">
    <span class="octicon octicon-question"></span>
  </span>


  <input type="hidden" name="ref" value="cmdform">

</form>
        <ul class="top-nav">
          <li class="explore"><a href="/explore">Explore</a></li>
            <li><a href="https://gist.github.com">Gist</a></li>
            <li><a href="/blog">Blog</a></li>
          <li><a href="https://help.github.com">Help</a></li>
        </ul>
      </div>

    


  <ul id="user-links">
    <li>
      <a href="/andreas-hjortgaard" class="name">
        <img height="20" src="https://0.gravatar.com/avatar/d7f2d593145994ad53cc0185e45406cf?d=https%3A%2F%2Fidenticons.github.com%2Fb419a9b6f50a8d7aff84ca3a5682100f.png&amp;s=140" width="20" /> andreas-hjortgaard
      </a>
    </li>

      <li>
        <a href="/new" id="new_repo" class="tooltipped downwards" title="Create a new repo" aria-label="Create a new repo">
          <span class="octicon octicon-repo-create"></span>
        </a>
      </li>

      <li>
        <a href="/settings/profile" id="account_settings"
          class="tooltipped downwards"
          aria-label="Account settings "
          title="Account settings ">
          <span class="octicon octicon-tools"></span>
        </a>
      </li>
      <li>
        <a class="tooltipped downwards" href="/logout" data-method="post" id="logout" title="Sign out" aria-label="Sign out">
          <span class="octicon octicon-log-out"></span>
        </a>
      </li>

  </ul>

<div class="js-new-dropdown-contents hidden">
  

<ul class="dropdown-menu">
  <li>
    <a href="/new"><span class="octicon octicon-repo-create"></span> New repository</a>
  </li>
  <li>
    <a href="/organizations/new"><span class="octicon octicon-organization"></span> New organization</a>
  </li>



    <li class="section-title">
      <span title="andreas-hjortgaard/ruby_scikit_learn">This repository</span>
    </li>
    <li>
      <a href="/andreas-hjortgaard/ruby_scikit_learn/issues/new"><span class="octicon octicon-issue-opened"></span> New issue</a>
    </li>
      <li>
        <a href="/andreas-hjortgaard/ruby_scikit_learn/settings/collaboration"><span class="octicon octicon-person-add"></span> New collaborator</a>
      </li>
</ul>

</div>


    
  </div>
</div>

      

      




          <div class="site" itemscope itemtype="http://schema.org/WebPage">
    
    <div class="pagehead repohead instapaper_ignore readability-menu">
      <div class="container">
        

<ul class="pagehead-actions">

    <li class="subscription">
      <form accept-charset="UTF-8" action="/notifications/subscribe" class="js-social-container" data-autosubmit="true" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="authenticity_token" type="hidden" value="hUoikWuKrKcXXO8NJ7elQLZNp0Fm3hmCkPpjxF9CpY4=" /></div>  <input id="repository_id" name="repository_id" type="hidden" value="12546664" />

    <div class="select-menu js-menu-container js-select-menu">
        <a class="social-count js-social-count" href="/andreas-hjortgaard/ruby_scikit_learn/watchers">
          1
        </a>
      <span class="minibutton select-menu-button with-count js-menu-target">
        <span class="js-select-button">
          <span class="octicon octicon-eye-unwatch"></span>
          Unwatch
        </span>
      </span>

      <div class="select-menu-modal-holder">
        <div class="select-menu-modal subscription-menu-modal js-menu-content">
          <div class="select-menu-header">
            <span class="select-menu-title">Notification status</span>
            <span class="octicon octicon-remove-close js-menu-close"></span>
          </div> <!-- /.select-menu-header -->

          <div class="select-menu-list js-navigation-container">

            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <div class="select-menu-item-text">
                <input id="do_included" name="do" type="radio" value="included" />
                <h4>Not watching</h4>
                <span class="description">You only receive notifications for discussions in which you participate or are @mentioned.</span>
                <span class="js-select-button-text hidden-select-button-text">
                  <span class="octicon octicon-eye-watch"></span>
                  Watch
                </span>
              </div>
            </div> <!-- /.select-menu-item -->

            <div class="select-menu-item js-navigation-item selected">
              <span class="select-menu-item-icon octicon octicon octicon-check"></span>
              <div class="select-menu-item-text">
                <input checked="checked" id="do_subscribed" name="do" type="radio" value="subscribed" />
                <h4>Watching</h4>
                <span class="description">You receive notifications for all discussions in this repository.</span>
                <span class="js-select-button-text hidden-select-button-text">
                  <span class="octicon octicon-eye-unwatch"></span>
                  Unwatch
                </span>
              </div>
            </div> <!-- /.select-menu-item -->

            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <div class="select-menu-item-text">
                <input id="do_ignore" name="do" type="radio" value="ignore" />
                <h4>Ignoring</h4>
                <span class="description">You do not receive any notifications for discussions in this repository.</span>
                <span class="js-select-button-text hidden-select-button-text">
                  <span class="octicon octicon-mute"></span>
                  Stop ignoring
                </span>
              </div>
            </div> <!-- /.select-menu-item -->

          </div> <!-- /.select-menu-list -->

        </div> <!-- /.select-menu-modal -->
      </div> <!-- /.select-menu-modal-holder -->
    </div> <!-- /.select-menu -->

</form>
    </li>

  <li>
  
<div class="js-toggler-container js-social-container starring-container ">
  <a href="/andreas-hjortgaard/ruby_scikit_learn/unstar" class="minibutton with-count js-toggler-target star-button starred upwards" title="Unstar this repo" data-remote="true" data-method="post" rel="nofollow">
    <span class="octicon octicon-star-delete"></span><span class="text">Unstar</span>
  </a>
  <a href="/andreas-hjortgaard/ruby_scikit_learn/star" class="minibutton with-count js-toggler-target star-button unstarred upwards" title="Star this repo" data-remote="true" data-method="post" rel="nofollow">
    <span class="octicon octicon-star"></span><span class="text">Star</span>
  </a>
  <a class="social-count js-social-count" href="/andreas-hjortgaard/ruby_scikit_learn/stargazers">0</a>
</div>

  </li>


        <li>
          <a href="/andreas-hjortgaard/ruby_scikit_learn/fork" class="minibutton with-count js-toggler-target fork-button lighter upwards" title="Fork this repo" rel="facebox nofollow">
            <span class="octicon octicon-git-branch-create"></span><span class="text">Fork</span>
          </a>
          <a href="/andreas-hjortgaard/ruby_scikit_learn/network" class="social-count">2</a>
        </li>


</ul>

        <h1 itemscope itemtype="http://data-vocabulary.org/Breadcrumb" class="entry-title public">
          <span class="repo-label"><span>public</span></span>
          <span class="mega-octicon octicon-repo-forked"></span>
          <span class="author">
            <a href="/andreas-hjortgaard" class="url fn" itemprop="url" rel="author"><span itemprop="title">andreas-hjortgaard</span></a></span
          ><span class="repohead-name-divider">/</span><strong
          ><a href="/andreas-hjortgaard/ruby_scikit_learn" class="js-current-repository js-repo-home-link">ruby_scikit_learn</a></strong>

          <span class="page-context-loader">
            <img alt="Octocat-spinner-32" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
          </span>

            <span class="fork-flag">
              <span class="text">forked from <a href="/ruby-scikit-learn/ruby_scikit_learn">ruby-scikit-learn/ruby_scikit_learn</a></span>
            </span>
        </h1>
      </div><!-- /.container -->
    </div><!-- /.repohead -->

    <div class="container">

      <div class="repository-with-sidebar repo-container ">

        <div class="repository-sidebar">
            

<div class="repo-nav repo-nav-full js-repository-container-pjax js-octicon-loaders">
  <div class="repo-nav-contents">
    <ul class="repo-menu">
      <li class="tooltipped leftwards" title="Code">
        <a href="/andreas-hjortgaard/ruby_scikit_learn" aria-label="Code" class="js-selected-navigation-item selected" data-gotokey="c" data-pjax="true" data-selected-links="repo_source repo_downloads repo_commits repo_tags repo_branches /andreas-hjortgaard/ruby_scikit_learn">
          <span class="octicon octicon-code"></span> <span class="full-word">Code</span>
          <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>


      <li class="tooltipped leftwards" title="Pull Requests"><a href="/andreas-hjortgaard/ruby_scikit_learn/pulls" aria-label="Pull Requests" class="js-selected-navigation-item js-disable-pjax" data-gotokey="p" data-selected-links="repo_pulls /andreas-hjortgaard/ruby_scikit_learn/pulls">
            <span class="octicon octicon-git-pull-request"></span> <span class="full-word">Pull Requests</span>
            <span class='counter'>0</span>
            <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>


        <li class="tooltipped leftwards" title="Wiki">
          <a href="/andreas-hjortgaard/ruby_scikit_learn/wiki" aria-label="Wiki" class="js-selected-navigation-item " data-pjax="true" data-selected-links="repo_wiki /andreas-hjortgaard/ruby_scikit_learn/wiki">
            <span class="octicon octicon-book"></span> <span class="full-word">Wiki</span>
            <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
</a>        </li>
    </ul>
    <div class="repo-menu-separator"></div>
    <ul class="repo-menu">

      <li class="tooltipped leftwards" title="Pulse">
        <a href="/andreas-hjortgaard/ruby_scikit_learn/pulse" aria-label="Pulse" class="js-selected-navigation-item " data-pjax="true" data-selected-links="pulse /andreas-hjortgaard/ruby_scikit_learn/pulse">
          <span class="octicon octicon-pulse"></span> <span class="full-word">Pulse</span>
          <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>

      <li class="tooltipped leftwards" title="Graphs">
        <a href="/andreas-hjortgaard/ruby_scikit_learn/graphs" aria-label="Graphs" class="js-selected-navigation-item " data-pjax="true" data-selected-links="repo_graphs repo_contributors /andreas-hjortgaard/ruby_scikit_learn/graphs">
          <span class="octicon octicon-graph"></span> <span class="full-word">Graphs</span>
          <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>

      <li class="tooltipped leftwards" title="Network">
        <a href="/andreas-hjortgaard/ruby_scikit_learn/network" aria-label="Network" class="js-selected-navigation-item js-disable-pjax" data-selected-links="repo_network /andreas-hjortgaard/ruby_scikit_learn/network">
          <span class="octicon octicon-git-branch"></span> <span class="full-word">Network</span>
          <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>
    </ul>


      <div class="repo-menu-separator"></div>
      <ul class="repo-menu">
        <li class="tooltipped leftwards" title="Settings">
          <a href="/andreas-hjortgaard/ruby_scikit_learn/settings" data-pjax aria-label="Settings">
            <span class="octicon octicon-tools"></span> <span class="full-word">Settings</span>
            <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
          </a>
        </li>
      </ul>
  </div>
</div>

            <div class="only-with-full-nav">
              

  

<div class="clone-url "
  data-protocol-type="http"
  data-url="/users/set_protocol?protocol_selector=http&amp;protocol_type=push">
  <h3><strong>HTTPS</strong> clone URL</h3>

  <div class="clone-url-box">
    <input type="text" class="clone js-url-field"
           value="https://github.com/andreas-hjortgaard/ruby_scikit_learn.git" readonly="readonly">

    <span class="js-zeroclipboard url-box-clippy minibutton zeroclipboard-button" data-clipboard-text="https://github.com/andreas-hjortgaard/ruby_scikit_learn.git" data-copied-hint="copied!" title="copy to clipboard"><span class="octicon octicon-clippy"></span></span>
  </div>
</div>

  

<div class="clone-url open"
  data-protocol-type="ssh"
  data-url="/users/set_protocol?protocol_selector=ssh&amp;protocol_type=push">
  <h3><strong>SSH</strong> clone URL</h3>

  <div class="clone-url-box">
    <input type="text" class="clone js-url-field"
           value="git@github.com:andreas-hjortgaard/ruby_scikit_learn.git" readonly="readonly">

    <span class="js-zeroclipboard url-box-clippy minibutton zeroclipboard-button" data-clipboard-text="git@github.com:andreas-hjortgaard/ruby_scikit_learn.git" data-copied-hint="copied!" title="copy to clipboard"><span class="octicon octicon-clippy"></span></span>
  </div>
</div>

  

<div class="clone-url "
  data-protocol-type="subversion"
  data-url="/users/set_protocol?protocol_selector=subversion&amp;protocol_type=push">
  <h3><strong>Subversion</strong> checkout URL</h3>

  <div class="clone-url-box">
    <input type="text" class="clone js-url-field"
           value="https://github.com/andreas-hjortgaard/ruby_scikit_learn" readonly="readonly">

    <span class="js-zeroclipboard url-box-clippy minibutton zeroclipboard-button" data-clipboard-text="https://github.com/andreas-hjortgaard/ruby_scikit_learn" data-copied-hint="copied!" title="copy to clipboard"><span class="octicon octicon-clippy"></span></span>
  </div>
</div>



<p class="clone-options">You can clone with
    <a href="#" class="js-clone-selector" data-protocol="http">HTTPS</a>,
    <a href="#" class="js-clone-selector" data-protocol="ssh">SSH</a>,
    <a href="#" class="js-clone-selector" data-protocol="subversion">Subversion</a>,
  and <a href="https://help.github.com/articles/which-remote-url-should-i-use">other methods.</a>
</p>

  <a href="github-mac://openRepo/https://github.com/andreas-hjortgaard/ruby_scikit_learn" class="minibutton sidebar-button">
    <span class="octicon octicon-device-desktop"></span>
    Clone in Desktop
  </a>


                <a href="/andreas-hjortgaard/ruby_scikit_learn/archive/master.zip"
                   class="minibutton sidebar-button"
                   title="Download this repository as a zip file"
                   rel="nofollow">
                  <span class="octicon octicon-cloud-download"></span>
                  Download ZIP
                </a>
            </div>
        </div><!-- /.repository-sidebar -->

        <div id="js-repo-pjax-container" class="repository-content context-loader-container" data-pjax-container>
          


<!-- blob contrib key: blob_contributors:v21:e65209e2183a63a15b2d06d592028133 -->
<!-- blob contrib frag key: views10/v8/blob_contributors:v21:e65209e2183a63a15b2d06d592028133 -->

<p title="This is a placeholder element" class="js-history-link-replace hidden"></p>

<a href="/andreas-hjortgaard/ruby_scikit_learn/find/master" data-pjax data-hotkey="t" style="display:none">Show File Finder</a>

<div class="file-navigation">
  


<div class="select-menu js-menu-container js-select-menu" >
  <span class="minibutton select-menu-button js-menu-target" data-hotkey="w"
    data-master-branch="master"
    data-ref="master" role="button" aria-label="Switch branches or tags">
    <span class="octicon octicon-git-branch"></span>
    <i>branch:</i>
    <span class="js-select-button">master</span>
  </span>

  <div class="select-menu-modal-holder js-menu-content js-navigation-container" data-pjax>

    <div class="select-menu-modal">
      <div class="select-menu-header">
        <span class="select-menu-title">Switch branches/tags</span>
        <span class="octicon octicon-remove-close js-menu-close"></span>
      </div> <!-- /.select-menu-header -->

      <div class="select-menu-filters">
        <div class="select-menu-text-filter">
          <input type="text" aria-label="Find or create a branch…" id="context-commitish-filter-field" class="js-filterable-field js-navigation-enable" placeholder="Find or create a branch…">
        </div>
        <div class="select-menu-tabs">
          <ul>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="branches" class="js-select-menu-tab">Branches</a>
            </li>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="tags" class="js-select-menu-tab">Tags</a>
            </li>
          </ul>
        </div><!-- /.select-menu-tabs -->
      </div><!-- /.select-menu-filters -->

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="branches">

        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


            <div class="select-menu-item js-navigation-item selected">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/andreas-hjortgaard/ruby_scikit_learn/blob/master/scikit-example/digit_classification.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="master" data-skip-pjax="true" rel="nofollow" title="master">master</a>
            </div> <!-- /.select-menu-item -->
        </div>

          <form accept-charset="UTF-8" action="/andreas-hjortgaard/ruby_scikit_learn/branches" class="js-create-branch select-menu-item select-menu-new-item-form js-navigation-item js-new-item-form" method="post"><div style="margin:0;padding:0;display:inline"><input name="authenticity_token" type="hidden" value="hUoikWuKrKcXXO8NJ7elQLZNp0Fm3hmCkPpjxF9CpY4=" /></div>
            <span class="octicon octicon-git-branch-create select-menu-item-icon"></span>
            <div class="select-menu-item-text">
              <h4>Create branch: <span class="js-new-item-name"></span></h4>
              <span class="description">from ‘master’</span>
            </div>
            <input type="hidden" name="name" id="name" class="js-new-item-value">
            <input type="hidden" name="branch" id="branch" value="master" />
            <input type="hidden" name="path" id="branch" value="scikit-example/digit_classification.py" />
          </form> <!-- /.select-menu-item -->

      </div> <!-- /.select-menu-list -->

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="tags">
        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


        </div>

        <div class="select-menu-no-results">Nothing to show</div>
      </div> <!-- /.select-menu-list -->

    </div> <!-- /.select-menu-modal -->
  </div> <!-- /.select-menu-modal-holder -->
</div> <!-- /.select-menu -->

  <div class="breadcrumb">
    <span class='repo-root js-repo-root'><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/andreas-hjortgaard/ruby_scikit_learn" data-branch="master" data-direction="back" data-pjax="true" itemscope="url"><span itemprop="title">ruby_scikit_learn</span></a></span></span><span class="separator"> / </span><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/andreas-hjortgaard/ruby_scikit_learn/tree/master/scikit-example" data-branch="master" data-direction="back" data-pjax="true" itemscope="url"><span itemprop="title">scikit-example</span></a></span><span class="separator"> / </span><strong class="final-path">digit_classification.py</strong> <span class="js-zeroclipboard minibutton zeroclipboard-button" data-clipboard-text="scikit-example/digit_classification.py" data-copied-hint="copied!" title="copy to clipboard"><span class="octicon octicon-clippy"></span></span>
  </div>
</div>


  <div class="commit commit-loader file-history-tease js-deferred-content" data-url="/andreas-hjortgaard/ruby_scikit_learn/contributors/master/scikit-example/digit_classification.py">
    Fetching contributors…

    <div class="participation">
      <p class="loader-loading"><img alt="Octocat-spinner-32-eaf2f5" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32-EAF2F5.gif" width="16" /></p>
      <p class="loader-error">Cannot retrieve contributors at this time</p>
    </div>
  </div>

<div id="files" class="bubble">
  <div class="file">
    <div class="meta">
      <div class="info">
        <span class="icon"><b class="octicon octicon-file-text"></b></span>
        <span class="mode" title="File Mode">file</span>
          <span>57 lines (43 sloc)</span>
        <span>1.597 kb</span>
      </div>
      <div class="actions">
        <div class="button-group">
                <a class="minibutton"
                   href="/andreas-hjortgaard/ruby_scikit_learn/edit/master/scikit-example/digit_classification.py"
                   data-method="post" rel="nofollow" data-hotkey="e">Edit</a>
          <a href="/andreas-hjortgaard/ruby_scikit_learn/raw/master/scikit-example/digit_classification.py" class="button minibutton " id="raw-url">Raw</a>
            <a href="/andreas-hjortgaard/ruby_scikit_learn/blame/master/scikit-example/digit_classification.py" class="button minibutton ">Blame</a>
          <a href="/andreas-hjortgaard/ruby_scikit_learn/commits/master/scikit-example/digit_classification.py" class="button minibutton " rel="nofollow">History</a>
        </div><!-- /.button-group -->
            <a class="minibutton danger empty-icon tooltipped downwards"
               href="/andreas-hjortgaard/ruby_scikit_learn/delete/master/scikit-example/digit_classification.py"
               title=""
               data-method="post" data-test-id="delete-blob-file" rel="nofollow">
            Delete
          </a>
      </div><!-- /.actions -->

    </div>
        <div class="blob-wrapper data type-python js-blob-data">
        <table class="file-code file-diff">
          <tr class="file-code-line">
            <td class="blob-line-nums">
              <span id="L1" rel="#L1">1</span>
<span id="L2" rel="#L2">2</span>
<span id="L3" rel="#L3">3</span>
<span id="L4" rel="#L4">4</span>
<span id="L5" rel="#L5">5</span>
<span id="L6" rel="#L6">6</span>
<span id="L7" rel="#L7">7</span>
<span id="L8" rel="#L8">8</span>
<span id="L9" rel="#L9">9</span>
<span id="L10" rel="#L10">10</span>
<span id="L11" rel="#L11">11</span>
<span id="L12" rel="#L12">12</span>
<span id="L13" rel="#L13">13</span>
<span id="L14" rel="#L14">14</span>
<span id="L15" rel="#L15">15</span>
<span id="L16" rel="#L16">16</span>
<span id="L17" rel="#L17">17</span>
<span id="L18" rel="#L18">18</span>
<span id="L19" rel="#L19">19</span>
<span id="L20" rel="#L20">20</span>
<span id="L21" rel="#L21">21</span>
<span id="L22" rel="#L22">22</span>
<span id="L23" rel="#L23">23</span>
<span id="L24" rel="#L24">24</span>
<span id="L25" rel="#L25">25</span>
<span id="L26" rel="#L26">26</span>
<span id="L27" rel="#L27">27</span>
<span id="L28" rel="#L28">28</span>
<span id="L29" rel="#L29">29</span>
<span id="L30" rel="#L30">30</span>
<span id="L31" rel="#L31">31</span>
<span id="L32" rel="#L32">32</span>
<span id="L33" rel="#L33">33</span>
<span id="L34" rel="#L34">34</span>
<span id="L35" rel="#L35">35</span>
<span id="L36" rel="#L36">36</span>
<span id="L37" rel="#L37">37</span>
<span id="L38" rel="#L38">38</span>
<span id="L39" rel="#L39">39</span>
<span id="L40" rel="#L40">40</span>
<span id="L41" rel="#L41">41</span>
<span id="L42" rel="#L42">42</span>
<span id="L43" rel="#L43">43</span>
<span id="L44" rel="#L44">44</span>
<span id="L45" rel="#L45">45</span>
<span id="L46" rel="#L46">46</span>
<span id="L47" rel="#L47">47</span>
<span id="L48" rel="#L48">48</span>
<span id="L49" rel="#L49">49</span>
<span id="L50" rel="#L50">50</span>
<span id="L51" rel="#L51">51</span>
<span id="L52" rel="#L52">52</span>
<span id="L53" rel="#L53">53</span>
<span id="L54" rel="#L54">54</span>
<span id="L55" rel="#L55">55</span>
<span id="L56" rel="#L56">56</span>
<span id="L57" rel="#L57">57</span>

            </td>
            <td class="blob-line-code">
                    <div class="highlight"><pre><div class='line' id='LC1'><span class="c"># -*- encoding: utf-8 -*-</span></div><div class='line' id='LC2'><br/></div><div class='line' id='LC3'><span class="kn">import</span> <span class="nn">numpy</span> <span class="kn">as</span> <span class="nn">np</span></div><div class='line' id='LC4'><span class="kn">from</span> <span class="nn">sklearn.linear_model</span> <span class="kn">import</span> <span class="n">LogisticRegression</span></div><div class='line' id='LC5'><span class="kn">from</span> <span class="nn">sklearn.cross_validation</span> <span class="kn">import</span> <span class="n">StratifiedKFold</span><span class="p">,</span> <span class="n">cross_val_score</span></div><div class='line' id='LC6'><br/></div><div class='line' id='LC7'><span class="c"># parameters</span></div><div class='line' id='LC8'><span class="n">num_train_samples</span> <span class="o">=</span> <span class="mi">1000</span></div><div class='line' id='LC9'><span class="n">num_test_samples</span> <span class="o">=</span> <span class="mi">500</span></div><div class='line' id='LC10'><br/></div><div class='line' id='LC11'><span class="c"># import data</span></div><div class='line' id='LC12'><span class="c"># download data from http://www.kaggle.com/c/digit-recognizer</span></div><div class='line' id='LC13'><span class="k">print</span> <span class="s">&quot;Loading training data...&quot;</span></div><div class='line' id='LC14'><span class="n">train_data</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">genfromtxt</span><span class="p">(</span><span class="s">&quot;train.csv&quot;</span><span class="p">,</span> <span class="n">delimiter</span><span class="o">=</span><span class="s">&#39;,&#39;</span><span class="p">,</span> <span class="n">skip_header</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span> </div><div class='line' id='LC15'><br/></div><div class='line' id='LC16'><span class="n">X_train</span> <span class="o">=</span> <span class="n">train_data</span><span class="p">[:</span><span class="n">num_train_samples</span><span class="p">,</span><span class="mi">1</span><span class="p">:]</span></div><div class='line' id='LC17'><span class="n">y_train</span> <span class="o">=</span> <span class="n">train_data</span><span class="p">[:</span><span class="n">num_train_samples</span><span class="p">,</span><span class="mi">0</span><span class="p">]</span></div><div class='line' id='LC18'><br/></div><div class='line' id='LC19'><br/></div><div class='line' id='LC20'><span class="k">print</span> <span class="s">&quot;Training size:&quot;</span></div><div class='line' id='LC21'><span class="k">print</span> <span class="n">X_train</span><span class="o">.</span><span class="n">shape</span></div><div class='line' id='LC22'><span class="k">print</span> <span class="n">y_train</span><span class="o">.</span><span class="n">shape</span></div><div class='line' id='LC23'><br/></div><div class='line' id='LC24'><span class="c"># train classifier using cross-validation</span></div><div class='line' id='LC25'><span class="k">print</span> <span class="s">&quot;Performing cross-validation...&quot;</span></div><div class='line' id='LC26'><span class="n">skf</span> <span class="o">=</span> <span class="n">StratifiedKFold</span><span class="p">(</span><span class="n">y_train</span><span class="p">,</span> <span class="n">n_folds</span><span class="o">=</span><span class="mi">5</span><span class="p">)</span></div><div class='line' id='LC27'><br/></div><div class='line' id='LC28'><span class="n">cs</span> <span class="o">=</span> <span class="p">[</span><span class="mf">1e-8</span><span class="p">,</span> <span class="mf">1e-7</span><span class="p">,</span> <span class="mf">1e-6</span><span class="p">,</span> <span class="mf">1e-5</span><span class="p">,</span> <span class="mf">1e-4</span><span class="p">,</span> <span class="mf">1e-3</span><span class="p">,</span> <span class="mf">1e-2</span><span class="p">,</span> <span class="mf">1e-1</span><span class="p">,</span> <span class="mf">1.0</span><span class="p">]</span></div><div class='line' id='LC29'><span class="n">best_score</span> <span class="o">=</span> <span class="mf">0.0</span></div><div class='line' id='LC30'><span class="k">for</span> <span class="n">c</span> <span class="ow">in</span> <span class="n">cs</span><span class="p">:</span></div><div class='line' id='LC31'>	<span class="n">logreg</span> <span class="o">=</span> <span class="n">LogisticRegression</span><span class="p">(</span><span class="n">penalty</span><span class="o">=</span><span class="s">&#39;l2&#39;</span><span class="p">,</span> <span class="n">C</span><span class="o">=</span><span class="n">c</span><span class="p">,</span> <span class="n">fit_intercept</span><span class="o">=</span><span class="bp">False</span><span class="p">)</span></div><div class='line' id='LC32'>	<span class="n">scores</span> <span class="o">=</span> <span class="n">cross_val_score</span><span class="p">(</span><span class="n">estimator</span><span class="o">=</span><span class="n">logreg</span><span class="p">,</span> <span class="n">X</span><span class="o">=</span><span class="n">X_train</span><span class="p">,</span> <span class="n">y</span><span class="o">=</span><span class="n">y_train</span><span class="p">,</span> <span class="n">cv</span><span class="o">=</span><span class="n">skf</span><span class="p">)</span> </div><div class='line' id='LC33'><br/></div><div class='line' id='LC34'>	<span class="n">score</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">mean</span><span class="p">(</span><span class="n">scores</span><span class="p">)</span></div><div class='line' id='LC35'><br/></div><div class='line' id='LC36'>	<span class="k">print</span> <span class="s">&quot;Score with C=</span><span class="si">%s</span><span class="s">: </span><span class="si">%s</span><span class="s">&quot;</span> <span class="o">%</span> <span class="p">(</span><span class="n">c</span><span class="p">,</span> <span class="n">score</span><span class="p">)</span></div><div class='line' id='LC37'>	<span class="k">if</span> <span class="n">score</span> <span class="o">&gt;</span> <span class="n">best_score</span><span class="p">:</span></div><div class='line' id='LC38'>		<span class="n">best_c</span> <span class="o">=</span> <span class="n">c</span></div><div class='line' id='LC39'>		<span class="n">best_score</span> <span class="o">=</span> <span class="n">score</span></div><div class='line' id='LC40'><br/></div><div class='line' id='LC41'><span class="k">print</span> <span class="s">&quot;Best c:     </span><span class="si">%s</span><span class="s">&quot;</span> <span class="o">%</span> <span class="n">best_c</span></div><div class='line' id='LC42'><span class="k">print</span> <span class="s">&quot;Best score: </span><span class="si">%s</span><span class="s">&quot;</span> <span class="o">%</span> <span class="n">best_score</span>  </div><div class='line' id='LC43'><br/></div><div class='line' id='LC44'><span class="c"># retrain with best C</span></div><div class='line' id='LC45'><span class="k">print</span> <span class="s">&quot;Retraining with C = </span><span class="si">%s</span><span class="s">&quot;</span> <span class="o">%</span> <span class="n">best_c</span></div><div class='line' id='LC46'><span class="n">best_logreg</span> <span class="o">=</span> <span class="n">LogisticRegression</span><span class="p">(</span><span class="n">penalty</span><span class="o">=</span><span class="s">&#39;l2&#39;</span><span class="p">,</span> <span class="n">C</span><span class="o">=</span><span class="n">best_c</span><span class="p">,</span> <span class="n">fit_intercept</span><span class="o">=</span><span class="bp">False</span><span class="p">)</span></div><div class='line' id='LC47'><span class="n">best_logreg</span><span class="o">.</span><span class="n">fit</span><span class="p">(</span><span class="n">X_train</span><span class="p">,</span> <span class="n">y_train</span><span class="p">)</span></div><div class='line' id='LC48'><br/></div><div class='line' id='LC49'><span class="c"># load test set</span></div><div class='line' id='LC50'><span class="k">print</span> <span class="s">&quot;Loading test data...&quot;</span></div><div class='line' id='LC51'><span class="n">test_data</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">genfromtxt</span><span class="p">(</span><span class="s">&quot;test.csv&quot;</span><span class="p">,</span> <span class="n">delimiter</span><span class="o">=</span><span class="s">&#39;,&#39;</span><span class="p">,</span> <span class="n">skip_header</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span> </div><div class='line' id='LC52'><span class="n">X_test</span> <span class="o">=</span> <span class="n">test_data</span><span class="p">[:</span><span class="n">num_test_samples</span><span class="p">,:]</span></div><div class='line' id='LC53'><span class="k">print</span> <span class="n">X_test</span><span class="o">.</span><span class="n">shape</span></div><div class='line' id='LC54'><br/></div><div class='line' id='LC55'><span class="k">print</span> <span class="s">&quot;Predicting test data...&quot;</span></div><div class='line' id='LC56'><span class="n">y_pred</span> <span class="o">=</span> <span class="n">best_logreg</span><span class="o">.</span><span class="n">predict</span><span class="p">(</span><span class="n">X_test</span><span class="p">)</span></div><div class='line' id='LC57'><span class="n">np</span><span class="o">.</span><span class="n">savetxt</span><span class="p">(</span><span class="s">&quot;test_predictions.csv&quot;</span><span class="p">,</span> <span class="n">y_pred</span><span class="p">,</span> <span class="n">delimiter</span><span class="o">=</span><span class="s">&quot;,&quot;</span><span class="p">)</span></div></pre></div>
            </td>
          </tr>
        </table>
  </div>

  </div>
</div>

<a href="#jump-to-line" rel="facebox[.linejump]" data-hotkey="l" class="js-jump-to-line" style="display:none">Jump to Line</a>
<div id="jump-to-line" style="display:none">
  <form accept-charset="UTF-8" class="js-jump-to-line-form">
    <input class="linejump-input js-jump-to-line-field" type="text" placeholder="Jump to line&hellip;" autofocus>
    <button type="submit" class="button">Go</button>
  </form>
</div>

        </div>

      </div><!-- /.repo-container -->
      <div class="modal-backdrop"></div>
    </div><!-- /.container -->
  </div><!-- /.site -->


    </div><!-- /.wrapper -->

      <div class="container">
  <div class="site-footer">
    <ul class="site-footer-links right">
      <li><a href="https://status.github.com/">Status</a></li>
      <li><a href="http://developer.github.com">API</a></li>
      <li><a href="http://training.github.com">Training</a></li>
      <li><a href="http://shop.github.com">Shop</a></li>
      <li><a href="/blog">Blog</a></li>
      <li><a href="/about">About</a></li>

    </ul>

    <a href="/">
      <span class="mega-octicon octicon-mark-github"></span>
    </a>

    <ul class="site-footer-links">
      <li>&copy; 2013 <span title="0.07279s from github-fe119-cp1-prd.iad.github.net">GitHub</span>, Inc.</li>
        <li><a href="/site/terms">Terms</a></li>
        <li><a href="/site/privacy">Privacy</a></li>
        <li><a href="/security">Security</a></li>
        <li><a href="/contact">Contact</a></li>
    </ul>
  </div><!-- /.site-footer -->
</div><!-- /.container -->


    <div class="fullscreen-overlay js-fullscreen-overlay" id="fullscreen_overlay">
  <div class="fullscreen-container js-fullscreen-container">
    <div class="textarea-wrap">
      <textarea name="fullscreen-contents" id="fullscreen-contents" class="js-fullscreen-contents" placeholder="" data-suggester="fullscreen_suggester"></textarea>
          <div class="suggester-container">
              <div class="suggester fullscreen-suggester js-navigation-container" id="fullscreen_suggester"
                 data-url="/andreas-hjortgaard/ruby_scikit_learn/suggestions/commit">
              </div>
          </div>
    </div>
  </div>
  <div class="fullscreen-sidebar">
    <a href="#" class="exit-fullscreen js-exit-fullscreen tooltipped leftwards" title="Exit Zen Mode">
      <span class="mega-octicon octicon-screen-normal"></span>
    </a>
    <a href="#" class="theme-switcher js-theme-switcher tooltipped leftwards"
      title="Switch themes">
      <span class="octicon octicon-color-mode"></span>
    </a>
  </div>
</div>



    <div id="ajax-error-message" class="flash flash-error">
      <span class="octicon octicon-alert"></span>
      <a href="#" class="octicon octicon-remove-close close ajax-error-dismiss"></a>
      Something went wrong with that request. Please try again.
    </div>

    
  </body>
</html>

