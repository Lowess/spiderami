#!/usr/bin/env python
# -*- coding: utf-8 -*-

html_doc="""<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
    "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" id="sixapart-standard">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <meta name="generator" content="Movable Type Pro 4.25" />
    <link rel="stylesheet" href="http://alestic.com/styles.css" type="text/css" />
    <link rel="start" href="http://alestic.com/" title="Home" />
    <link rel="alternate" type="application/atom+xml" title="Recent Entries" href="http://feeds.alestic.com/alestic" />
    <script type="text/javascript" src="http://alestic.com/mt.js"></script>
    
    <script type="text/javascript">
    var adminurl = 'http://alestic.com/mt/' + 'mt.cgi';
    var blog_id = '1';
    var page_id = '';
    </script>
    
    <title>Using AWS with Ubuntu - Alestic.com</title>

<link rel="icon"          href="/img/alestic-favicon.png" type="image/png">

<!-- Google Analytics -->
<script>
  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

  ga('create', 'UA-93723-8', {
    'cookieDomain': 'alestic.com',
    'siteSpeedSampleRate': 100
  });
  ga('require', 'displayfeatures');
  ga('send', 'pageview');

  // based on http://support.google.com/analytics/bin/answer.py?hl=en&answer=1136920
  var sponsorClick = function(link, sponsor) {
    ga('send', 'event', 'Sponsor-Click', sponsor, {'hitCallback':
      function () {
        document.location = link.href;
      }
    });
  }
  var sponsorImpression = function(sponsor) {
    ga('send', 'event', 'Sponsor-Impression', sponsor, {'nonInteraction': 1});
  }
</script>

<!-- Google consumer surveys  -->
<script async="" defer="" src="//survey.g.doubleclick.net/async_survey?site=smyhxtzq4omrk"></script>

</head>
<body id="professional-website" class="mt-main-index layout-wm">
    <div id="container">
        <div id="container-inner">
            <div id="header">
                <div id="header-inner">
                    <div id="header-content">
<div class="header-right">
          <div>
            Thanks to sponsors...<br />


  <a href="http://aws.amazon.com/" target="_blank" rel="nofollow"
               onmousedown="this.href='/go?'+this.href"
               onclick="sponsorClick(this,'amazon');return false;"
               ><img width="190" height="60"
               src="/img/sponsor/amazon-web-services-sponsor.png" border="0"
               alt="Amazon Web Services"></a
    >
  <script type="text/javascript">sponsorImpression('amazon');</script>



         </div>
</div>

                        <a href="http://alestic.com/" accesskey="1"><h1 id="header-name">Alestic.com</h1>
</a>                        <h2 id="header-description"><a href="http://alestic.com/">Using Amazon AWS with Ubuntu</a></h2>

<!--
                        <div class="widget-sign-in widget">
    <h3 class="widget-header">Sign In</h3>
    <div id="signin-widget-content" class="widget-content"></div>
</div>
<script type="text/javascript">
/* <![CDATA[ */
function mtUpdateSignInWidget(u) {
    var el = document.getElementById('signin-widget-content');
    var content = '';
    if (!el) return;
    if (u) {
        if (u && u.is_authenticated) {
            user = u;
            mtSaveUser();
        } else {
            // user really isn't logged in; so let's do this!
            return mtSignIn();
        }
    } else {
        u = mtGetUser();
    }
    if (u && u.name) {
        var url;
        if (u.is_authenticated) {
            if (u.is_author) {
                url = 'http://alestic.com/mt/mt-comments.cgi?__mode=edit_profile&blog_id=1';
                url += '&static=' + encodeURIComponent( location.href );
            } else {
                url = u.url;
            }
        } else if (u.url) {
            url = u.url;
        } else {
            url = null;
        }
        var content = 'You are signed in as ';
        if (url)
            content += '<a href="' + url + '">' + u.name + '</a>';
        else
            content += u.name;
        content += '.  (<a href="javascript:void(0)" onclick="return mtSignOutOnClick()">sign out</a>)';
    } else if (u && u.is_banned) {
        content = 'You do not have permission to sign in to this blog.';
    } else {
        content = '<a href="javascript:void(0)" onclick="return mtSignInOnClick(\'signin-widget-content\')">Sign In</a>';
    }
    el.innerHTML = content;
}
mtAttachEvent('usersignin', mtUpdateSignInWidget);
mtUpdateSignInWidget();
/* ]]> */
</script>

-->
                    </div>
                </div>
            </div>
            <div id="main-navigation">
                <div id="main-navigation-inner">


<ul>
    <li style="margin:5px 10px 0px 20px">
          <g:plusone size="tall" annotation="inline" width="300" href="http://alestic.com/"></g:plusone>
    </li>

</ul>
                    <!-- 
<ul>
    <li class="first on"><a href="http://alestic.com/index.html">Home</a></li>

    <li class=""><a href="http://alestic.com/blog/">Blog</a></li>

    
    
    
    
    <li class=""><a href="http://alestic.com/sponsors">Sponsors</a></li>
    

    
    
    <li class="last"><a href="http://alestic.com/support">Support</a></li>
    

</ul>
-->

                    <div class="widget-search widget">
    <h3 class="widget-header">Search</h3>
    <div class="widget-content">
        <form method="get" action="http://alestic.com/mt/mt-search.cgi">
            <input type="text" id="search" class="ti" name="search" value="" />

            <input type="hidden" name="IncludeBlogs" value="1" />

            <input type="hidden" name="limit" value="20" />
            <input type="submit" accesskey="4" value="Search" />
        </form>
    </div>
</div>


<ul>
    <li class="first"><a href="http://alestic.com/archives.html">Archives</a></li>

    
    
    <li class="last"><a href="http://alestic.com/sponsors">Sponsors</a></li>
    
</ul>
                </div>
            </div>
            <div id="content">
                <div id="content-inner">

                    <div id="homepage-image">&nbsp;</div>

                    <div id="alpha">
                        <div id="alpha-inner">

<div class="asset-footer"></div>


    <!--
<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
         xmlns:trackback="http://madskills.com/public/xml/rss/module/trackback/"
         xmlns:dc="http://purl.org/dc/elements/1.1/">
<rdf:Description
    rdf:about="http://alestic.com/2015/04/aws-cli-sns-lambda"
    trackback:ping="http://alestic.com/mt/mt-tb.cgi/168"
    dc:title="Subscribing AWS Lambda Function To SNS Topic With aws-cli"
    dc:identifier="http://alestic.com/2015/04/aws-cli-sns-lambda"
    dc:subject="Lambda"
    dc:description="The aws-cli documentation and command line help text have not been updated yet to include the syntax for subscribing an AWS Lambda function to an SNS topic, but it does work! Here&#8217;s the format: aws sns subscribe \ -topic-arn arn:aws:sns:REGION:ACCOUNT:SNSTOPIC..."
    dc:creator="Eric Hammond"
    dc:date="2015-04-13T17:35:34-08:00" />
</rdf:RDF>
-->

<div id="entry-180" class="entry-asset asset hentry">
    <div class="asset-header">
        <h2 class="asset-name entry-title"><a href="http://alestic.com/2015/04/aws-cli-sns-lambda" rel="bookmark">Subscribing AWS Lambda Function To SNS Topic With aws-cli</a>
        <!-- Google +1 -->
<!-- 
        <g:plusone size="medium" href="http://alestic.com/2015/04/aws-cli-sns-lambda"></g:plusone>
-->
        </h2>
        <div class="asset-meta">
    <span class="byline">

        By <span class="vcard author"><a rel="author" href="https://plus.google.com/111045584683584396225/about" class="fn url">Eric Hammond</a></span> on <abbr class="published" title="2015-04-13T17:35:34-08:00">April 13, 2015  5:35 PM</abbr>

    </span>

    <span class="separator">|</span> <a href="http://alestic.com/2015/04/aws-cli-sns-lambda#comments">0 Comments</a>
<!--
    <span class="separator">|</span> <a href="http://alestic.com/2015/04/aws-cli-sns-lambda#trackbacks">0 TrackBacks</a>
-->

</div>

    </div>
    <div class="asset-content entry-content">

        <div class="asset-body">
            <p>The <a href="http://docs.aws.amazon.com/cli/latest/reference/sns/subscribe.html">aws-cli documentation</a> and command line help text have not been updated yet to include the syntax for subscribing an AWS Lambda function to an SNS topic, but it does work!</p>

<p>Here&#8217;s the format:</p>

<pre><code>aws sns subscribe   --topic-arn arn:aws:sns:REGION:ACCOUNT:SNSTOPIC   --protocol lambda   --notification-endpoint arn:aws:lambda:REGION:ACCOUNT:function:LAMBDAFUNCTION
</code></pre>

<p>where REGION, ACCOUNT, SNSTOPIC, and LAMBDAFUNCTION are substituted with appropriate values for your account.</p>

<p>For example: </p>

<pre><code>aws sns subscribe --topic-arn arn:aws:sns:us-east-1:012345678901:mytopic   --protocol lambda   --notification-endpoint arn:aws:lambda:us-east-1:012345678901:function:myfunction
</code></pre>

<p>This returns an SNS subscription ARN like so:</p>

<pre><code>{
    "SubscriptionArn": "arn:aws:sns:us-east-1:012345678901:mytopic:2ced0134-e247-11e4-9da9-22000b5b84fe"
}
</code></pre>

<p>You can unsubscribe with a command like:</p>

<pre><code>aws sns unsubscribe   --subscription-arn arn:aws:sns:us-east-1:012345678901:mytopic:2ced0134-e247-11e4-9da9-22000b5b84fe
</code></pre>

<p>where the subscription ARN is the one returned from the subscribe command.</p>

<p>I&#8217;m using the latest version of aws-cli as of 2015-04-15 on the GitHub &#8220;develop&#8221; branch, which is version 1.7.22.</p>

        </div>



    </div>
    <div class="asset-footer"></div>
</div>

    <!--
<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
         xmlns:trackback="http://madskills.com/public/xml/rss/module/trackback/"
         xmlns:dc="http://purl.org/dc/elements/1.1/">
<rdf:Description
    rdf:about="http://alestic.com/2015/04/aws-lambda-sns"
    trackback:ping="http://alestic.com/mt/mt-tb.cgi/167"
    dc:title="AWS Lambda Event-Driven Architecture With Amazon SNS"
    dc:identifier="http://alestic.com/2015/04/aws-lambda-sns"
    dc:subject="Lambda"
    dc:description="Today, Amazon announced that AWS Lambda functions can be subscribed to Amazon SNS topics. This means that any message posted to an SNS topic can trigger the execution of custom code you have written, but you don&#8217;t have to maintain..."
    dc:creator="Eric Hammond"
    dc:date="2015-04-09T12:43:00-08:00" />
</rdf:RDF>
-->

<div id="entry-179" class="entry-asset asset hentry">
    <div class="asset-header">
        <h2 class="asset-name entry-title"><a href="http://alestic.com/2015/04/aws-lambda-sns" rel="bookmark">AWS Lambda Event-Driven Architecture With Amazon SNS</a>
        <!-- Google +1 -->
<!-- 
        <g:plusone size="medium" href="http://alestic.com/2015/04/aws-lambda-sns"></g:plusone>
-->
        </h2>
        <div class="asset-meta">
    <span class="byline">

        By <span class="vcard author"><a rel="author" href="https://plus.google.com/111045584683584396225/about" class="fn url">Eric Hammond</a></span> on <abbr class="published" title="2015-04-09T12:43:00-08:00">April  9, 2015 12:43 PM</abbr>

    </span>

    <span class="separator">|</span> <a href="http://alestic.com/2015/04/aws-lambda-sns#comments">1 Comment</a>
<!--
    <span class="separator">|</span> <a href="http://alestic.com/2015/04/aws-lambda-sns#trackbacks">0 TrackBacks</a>
-->

</div>

    </div>
    <div class="asset-content entry-content">

        <div class="asset-body">
            <p>Today, Amazon announced that <a href="http://docs.aws.amazon.com/sns/latest/dg/sns-lambda.html">AWS Lambda functions can be subscribed to Amazon SNS topics</a>. </p>

<p>This means that any message posted to an SNS topic can trigger the execution of custom code you have written, but you don&#8217;t have to maintain any infrastructure to keep that code available to listen for those events and you don&#8217;t have to pay for any infrastructure when the code is not being run.</p>

<p>This is, in my opinion, the first time that Amazon can truly say that AWS Lambda is event-driven, as we now have a central, independent, event management system (SNS) where any authorized entity can trigger the event (post a message to a topic) and any authorized AWS Lambda function can listen for the event, and neither has to know about the other.</p>

<p>Making this instantly useful is the fact that there already are a number of AWS services and events that can post messages to Amazon SNS. This means there are a lot of application ideas that are ready to be implemented with nothing but a few commands to set up the SNS topic, and some snippets of nodejs code to upload as an AWS Lambda function.</p>

<p>Unfortunately, I was unable to find a comprehensive list of all the AWS services and events that can post messages to Amazon SNS (Simple Notification Service).</p>

<p>I&#8217;d like to try an experiment and ask the readers of this blog to submit pointers to AWS and other services which can be configured to post events to Amazon SNS. I will collect the list and update this blog post.</p>

<p>Here&#8217;s the list so far:</p>

<ul>
<li><p>Auto Scaling can post events to SNS when instances are launched or terminated. <a href="http://docs.aws.amazon.com/AutoScaling/latest/DeveloperGuide/ASGettingNotifications.html">http://docs.aws.amazon.com/AutoScaling/latest/DeveloperGuide/ASGettingNotifications.html</a></p></li>
<li><p>GitHub can post repository events to SNS. &#8220;Settings&#8221; / &#8220;Webhooks &amp; Services&#8221;</p></li>
<li><p>RDS (instance, security and parameter group and snapshots) can post to SNS topics. <a href="http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Events.html">http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Events.html</a></p></li>
<li><p>S3 can post messages to SNS when a Reduced Redundancy Storage (RRS) object is lost.
<a href="http://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html">http://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html</a></p></li>
<li><p>S3 can post messages to SNS when a new object is added to a bucket and when an existing object is updated. <a href="http://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html">http://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html</a></p></li>
<li><p>AWS CloudWatch (Logs) can trigger SNS messages. [TBD: specific event descriptions? links?]</p></li>
</ul>

<p>You can either submit your suggestions as comments on this blog post, or tweet the pointer mentioning <a href="https://twitter.com/esh">@esh</a></p>

<p>Thanks for contributing ideas:</p>

<ul>
<li><p><a href="https://twitter.com/pas256/">Peter Sankauskas</a></p></li>
<li><p><a href="https://twitter.com/FlexiAuthor/">Flexi Author</a></p></li>
<li><p>Anonymous commenter</p></li>
</ul>

<p><em>[2015-04-13: Updated with input from comments and Twitter]</em></p>

        </div>



    </div>
    <div class="asset-footer"></div>
</div>

    <!--
<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
         xmlns:trackback="http://madskills.com/public/xml/rss/module/trackback/"
         xmlns:dc="http://purl.org/dc/elements/1.1/">
<rdf:Description
    rdf:about="http://alestic.com/2014/12/aws-lambda-persistence"
    trackback:ping="http://alestic.com/mt/mt-tb.cgi/165"
    dc:title="Persistence Of The AWS Lambda Environment Between Function Invocations"
    dc:identifier="http://alestic.com/2014/12/aws-lambda-persistence"
    dc:subject="Lambda"
    dc:description="AWS Lambda functions are run inside of an Amazon Linux environment (presumably a container of some sort). Sequential calls to the same Lambda function could hit the same or different instantiations of the environment. If you hit the same copy..."
    dc:creator="Eric Hammond"
    dc:date="2014-12-10T08:00:00-08:00" />
</rdf:RDF>
-->

<div id="entry-177" class="entry-asset asset hentry">
    <div class="asset-header">
        <h2 class="asset-name entry-title"><a href="http://alestic.com/2014/12/aws-lambda-persistence" rel="bookmark">Persistence Of The AWS Lambda Environment Between Function Invocations</a>
        <!-- Google +1 -->
<!-- 
        <g:plusone size="medium" href="http://alestic.com/2014/12/aws-lambda-persistence"></g:plusone>
-->
        </h2>
        <div class="asset-meta">
    <span class="byline">

        By <span class="vcard author"><a rel="author" href="https://plus.google.com/111045584683584396225/about" class="fn url">Eric Hammond</a></span> on <abbr class="published" title="2014-12-10T08:00:00-08:00">December 10, 2014  8:00 AM</abbr>

    </span>

    <span class="separator">|</span> <a href="http://alestic.com/2014/12/aws-lambda-persistence#comments">0 Comments</a>
<!--
    <span class="separator">|</span> <a href="http://alestic.com/2014/12/aws-lambda-persistence#trackbacks">0 TrackBacks</a>
-->

</div>

    </div>
    <div class="asset-content entry-content">

        <div class="asset-body">
            <p>AWS Lambda functions are run inside of an Amazon Linux environment (presumably a container of some sort). Sequential calls to the same Lambda function could hit the same or different instantiations of the environment.</p>

<p>If you hit the same copy (I don&#8217;t want to say &#8220;instance&#8221;) of the Lambda function, then stuff you left in the environment from a previous run might still be available.</p>

<p>This could be useful (think caching) or hurtful (if your code incorrectly expects a fresh start every run).</p>

<p>Here&#8217;s an example using <a href="http://alestic.com/2014/11/aws-lambda-shell">lambdash</a>, a hack I wrote that sends shell commands to a Lambda function to be run in the AWS Lambda environment, with stdout/stderr being sent  back through S3 and displayed locally.</p>

<pre><code>$ lambdash 'echo a $(date) &gt;&gt; /tmp/run.log; cat /tmp/run.log'
a Tue Dec 9 13:54:50 PST 2014

$ lambdash 'echo b $(date) &gt;&gt; /tmp/run.log; cat /tmp/run.log'
a Tue Dec 9 13:54:50 PST 2014
b Tue Dec 9 13:55:00 PST 2014

$ lambdash 'echo c $(date) &gt;&gt; /tmp/run.log; cat /tmp/run.log'
a Tue Dec 9 13:54:50 PST 2014
b Tue Dec 9 13:55:00 PST 2014
c Tue Dec 9 13:55:20 PST 2014
</code></pre>

<p>As you can see in this example, the file in /tmp contains content from previous runs.</p>

<p>These tests are being run in AWS Lambda Preview, and should not be depended on for long term or production plans. Amazon could change how AWS Lambda works at any time for any reason, especially when the behaviors are not documented as part of the interface. For example, Amazon could decide to clear out writable file system areas like /tmp after each run.</p>

<p>If you want to have a dependable storage that can be shared among multiple copies of an AWS Lambda function, consider using standard AWS services like DynamoDB, RDS, ElastiCache, S3, etc.</p>

        </div>



    </div>
    <div class="asset-footer"></div>
</div>

    <!--
<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
         xmlns:trackback="http://madskills.com/public/xml/rss/module/trackback/"
         xmlns:dc="http://purl.org/dc/elements/1.1/">
<rdf:Description
    rdf:about="http://alestic.com/2014/12/ec2-reserved-instances"
    trackback:ping="http://alestic.com/mt/mt-tb.cgi/164"
    dc:title="Before You Buy Amazon EC2 (New) Reserved Instances"
    dc:identifier="http://alestic.com/2014/12/ec2-reserved-instances"
    dc:subject="EC2"
    dc:description="understand the commitment you are making to pay for the entire 1-3 years Amazon just announced a change in the way that Reserved Instances are sold. Instead of selling the old Reserved Instance types: Light Utilization Medium Utilization Heavy Utilization..."
    dc:creator="Eric Hammond"
    dc:date="2014-12-02T16:15:00-08:00" />
</rdf:RDF>
-->

<div id="entry-176" class="entry-asset asset hentry">
    <div class="asset-header">
        <h2 class="asset-name entry-title"><a href="http://alestic.com/2014/12/ec2-reserved-instances" rel="bookmark">Before You Buy Amazon EC2 (New) Reserved Instances</a>
        <!-- Google +1 -->
<!-- 
        <g:plusone size="medium" href="http://alestic.com/2014/12/ec2-reserved-instances"></g:plusone>
-->
        </h2>
        <div class="asset-meta">
    <span class="byline">

        By <span class="vcard author"><a rel="author" href="https://plus.google.com/111045584683584396225/about" class="fn url">Eric Hammond</a></span> on <abbr class="published" title="2014-12-02T16:15:00-08:00">December  2, 2014  4:15 PM</abbr>

    </span>

    <span class="separator">|</span> <a href="http://alestic.com/2014/12/ec2-reserved-instances#comments">0 Comments</a>
<!--
    <span class="separator">|</span> <a href="http://alestic.com/2014/12/ec2-reserved-instances#trackbacks">0 TrackBacks</a>
-->

</div>

    </div>
    <div class="asset-content entry-content">

        <div class="asset-body">
            <p><em>understand the commitment you are making to pay for the entire 1-3 years</em></p>

<p>Amazon just announced a change in the way that Reserved Instances are sold. Instead of selling the old Reserved Instance types:</p>

<ul>
<li>Light Utilization</li>
<li>Medium Utilization</li>
<li>Heavy Utilization</li>
</ul>

<p>EC2 is now selling these new Reserved Instance types:</p>

<ul>
<li>No Upfront</li>
<li>Partial Upfront</li>
<li>All Upfront</li>
</ul>

<p>Despite the fact that they are still called &#8220;Reserved Instances&#8221; and that there are three plans which sound like increasing commitment, the are not equivalent and do not map 1-1 old to new. In fact the new Reserved Instances are not even increasing commitment.</p>

<p>You should forget what you knew about Reserved Instances and read all the fine print before making any further Reserved Instance purchases.</p>

<p>One of the big differences between the old and the new is that you are always committing to spend the entire 1-3 years of cost even if you are not running a matching instance during part of that time. This text is buried in the fine print in a &#8220;**&#8221; footnote towards the bottom of the <a href="http://aws.amazon.com/ec2/pricing/">pricing page</a>:</p>

<blockquote>
  <p><strong>When you purchase a Reserved Instance, you are billed for every hour during the entire Reserved Instance term that you select, regardless of whether the instance is running or not.</strong></p>
</blockquote>

<p>As I pointed out in the 2012 article titled <a href="http://alestic.com/2012/09/ec2-reserved-instance-savings">Save Money by Giving Away Unused Heavy Utilization Reserved Instances</a>, this was also true of Heavy Utilization Reserved Instances, but with the old Light and Medium Utilization Reserved Instances you stopped spending money by stopping or terminating your instance.</p>

<p>Let&#8217;s walk through an example with the new EC2 Reserved Instance prices. Say you expect to run a c3.2xlarge for a year. Here are some options at the prices when this article was published:</p>

<table class="amis">
<thead>
 <tr>
   <th>Pricing Option</th>
   <th>Cost Structure</th>
   <th>Yearly Cost</th>
   <th>Savings over On Demand</th>
 </tr>
</thead>
<tbody>
 <tr>
  <td><b>On Demand</b></td>
  <td>$0.420/hour</td>
  <td>$3,679.20/year</td>
  <td>&nbsp;</td>
 </tr>
 <tr>
  <td><b>No Upfront RI</b></td>
  <td>$213.16/month</td>
  <td>$2,557.92/year</td>
  <td>30%</td>
 </tr>
 <tr>
  <td><b>Partial Upfront RI</b></td>
  <td>$1,304/once + $75.92/month</td>
  <td>$2,215.04/year</td>
  <td>40%</td>
 </tr>
 <tr>
  <td><b>All Upfront RI</b></td>
  <td>$2,170/once</td>
  <td>$2,170.00/year</td>
  <td>41%</td>
 </tr>
</tbody>
</table>

<p><p></p>

<p>There&#8217;s a big jump in yearly savings from On Demand to the Reserved Instances, and then there is an increasing (but sometimes small) savings for the more of the total cost you pay up front. The percentage savings varies by instance type, so read up on the <a href="http://aws.amazon.com/ec2/pricing/">pricing page</a>.</p>

<p>The big difference is that you can stop paying the On Demand price if you decide you don&#8217;t need that instance running, or you figure out that the application can work better on a larger (or smaller) instance type.</p>

<p>With all new Reserved Instance pricing options, you commit to paying the entire year&#8217;s cost. The only difference is how much of it you pay up front and how much you pay over the next 12 months.</p>

<p>If you purchase a Reserved Instance and decide you don&#8217;t need it after a while, you may be able to sell it (perhaps at some loss) on the Reserved Instance Marketplace, but your odds of completing a sale and the money you get back from that are not guaranteed.</p>

        </div>



    </div>
    <div class="asset-footer"></div>
</div>

    <!--
<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
         xmlns:trackback="http://madskills.com/public/xml/rss/module/trackback/"
         xmlns:dc="http://purl.org/dc/elements/1.1/">
<rdf:Description
    rdf:about="http://alestic.com/2014/12/s3-bucket-notification-to-sqssns-on-object-creation"
    trackback:ping="http://alestic.com/mt/mt-tb.cgi/163"
    dc:title="S3 Bucket Notification to SQS/SNS on Object Creation"
    dc:identifier="http://alestic.com/2014/12/s3-bucket-notification-to-sqssns-on-object-creation"
    dc:subject="S3"
    dc:description="A fantastic new and oft-requested AWS feature was released during AWS re:Invent, but has gotten lost in all the hype about AWS Lambda functions being triggered when objects are added to S3 buckets. AWS Lambda is currently in limited Preview..."
    dc:creator="Eric Hammond"
    dc:date="2014-12-01T08:00:00-08:00" />
</rdf:RDF>
-->

<div id="entry-175" class="entry-asset asset hentry">
    <div class="asset-header">
        <h2 class="asset-name entry-title"><a href="http://alestic.com/2014/12/s3-bucket-notification-to-sqssns-on-object-creation" rel="bookmark">S3 Bucket Notification to SQS/SNS on Object Creation</a>
        <!-- Google +1 -->
<!-- 
        <g:plusone size="medium" href="http://alestic.com/2014/12/s3-bucket-notification-to-sqssns-on-object-creation"></g:plusone>
-->
        </h2>
        <div class="asset-meta">
    <span class="byline">

        By <span class="vcard author"><a rel="author" href="https://plus.google.com/111045584683584396225/about" class="fn url">Eric Hammond</a></span> on <abbr class="published" title="2014-12-01T08:00:00-08:00">December  1, 2014  8:00 AM</abbr>

    </span>

    <span class="separator">|</span> <a href="http://alestic.com/2014/12/s3-bucket-notification-to-sqssns-on-object-creation#comments">0 Comments</a>
<!--
    <span class="separator">|</span> <a href="http://alestic.com/2014/12/s3-bucket-notification-to-sqssns-on-object-creation#trackbacks">0 TrackBacks</a>
-->

</div>

    </div>
    <div class="asset-content entry-content">

        <div class="asset-body">
            <p>A fantastic new and oft-requested AWS feature was released during AWS re:Invent, but has gotten lost in all the hype about AWS Lambda functions being triggered when objects are added to S3 buckets. AWS Lambda is currently in limited Preview mode and you have to request access, but this related feature is already available and ready to use.</p>

<p>I&#8217;m talking about automatic <a href="http://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html">S3 bucket notifications to SNS topics and SQS queues</a> when new S3 objects are added.</p>

<p>Unlike AWS Lambda, with S3 bucket notifications you do need to maintain the infrastructure to run your code, but you&#8217;re already running EC2 instances for application servers and job processing, so this will fit right in.</p>

<p>To detect and respond to S3 object creation in the past, you needed to either have every process that uploaded to S3 subsequently trigger your back end code in some way, or you needed to poll the S3 bucket to see if new objects had been added. The former adds code complexity and tight coupling dependencies. The latter can be costly in performance and latency, especially as the number of objects in the bucket grows.</p>

<p>With the new S3 bucket notification configuration options, the addition of an object to a bucket can send a message to an SNS topic or to an SQS queue, triggering your code quickly and effortlessly.</p>

<p>Here&#8217;s a working example of how to set up and use S3 bucket notification configurations to send messages to SNS on object creation and update.</p>

<h2>Setup</h2>

<p>Replace parameter values with your preferred names.</p>

<pre><code>region=us-east-1
s3_bucket_name=BUCKETNAMEHERE
email_address=YOURADDRESS@EXAMPLE.COM
sns_topic_name=s3-object-created-$(echo $s3_bucket_name | tr '.' '-')
sqs_queue_name=$sns_topic_name
</code></pre>

<p>Create the test bucket.</p>

<pre><code>aws s3 mb   --region "$region"   s3://$s3_bucket_name
</code></pre>

<p>Create an SNS topic.</p>

<pre><code>sns_topic_arn=$(aws sns create-topic   --region "$region"   --name "$sns_topic_name"   --output text   --query 'TopicArn')
echo sns_topic_arn=$sns_topic_arn
</code></pre>

<p>Allow S3 to publish to the SNS topic for activity in the specific S3 bucket.</p>

<pre><code>aws sns set-topic-attributes   --topic-arn "$sns_topic_arn"   --attribute-name Policy   --attribute-value '{
      "Version": "2008-10-17",
      "Id": "s3-publish-to-sns",
      "Statement": [{
              "Effect": "Allow",
              "Principal": { "AWS" : "*" },
              "Action": [ "SNS:Publish" ],
              "Resource": "'$sns_topic_arn'",
              "Condition": {
                  "ArnLike": {
                      "aws:SourceArn": "arn:aws:s3:*:*:'$s3_bucket_name'"
                  }
              }
      }]
  }'
</code></pre>

<p>Add a notification to the S3 bucket so that it sends messages to the
SNS topic when objects are created (or updated).</p>

<pre><code>aws s3api put-bucket-notification   --region "$region"   --bucket "$s3_bucket_name"   --notification-configuration '{
    "TopicConfiguration": {
      "Events": [ "s3:ObjectCreated:*" ],
      "Topic": "'$sns_topic_arn'"
    }
  }'
</code></pre>

<h2>Test</h2>

<p>You now have an S3 bucket that is going to post a message to an SNS topic when objects are added. Let&#8217;s give it a try by connecting an email address listener to the SNS topic.</p>

<p>Subscribe an email address to the SNS topic.</p>

<pre><code>aws sns subscribe   --topic-arn "$sns_topic_arn"   --protocol email   --notification-endpoint "$email_address"
</code></pre>

<p><strong>IMPORTANT! Go to your email inbox now and click the link to confirm
that you want to subscribe that email address to the SNS topic.</strong></p>

<p>Upload one or more files to the S3 bucket to trigger the SNS topic messages.</p>

<pre><code>aws s3 cp [SOMEFILE] s3://$s3_bucket_name/testfile-01
</code></pre>

<p>Check your email for the notification emails in JSON format, containing attributes like:</p>

<pre><code>{ "Records":[  
    { "eventTime":"2014-11-27T00:57:44.387Z",
      "eventName":"ObjectCreated:Put", ...
      "s3":{
        "bucket":{ "name":"BUCKETNAMEHERE", ... },
        "object":{ "key":"testfile-01", "size":5195, ... }
}}]}
</code></pre>

<h2>Notification to SQS</h2>

<p>The above example connects an SNS topic to the S3 bucket notification configuration. Amazon also supports having the bucket notifications go directly to an SQS queue, but I do not recommend it.</p>

<p>Instead, send the S3 bucket notification to SNS and have SNS forward it to SQS. This way, you can easily add other listeners to the SNS topic as desired. You can even have multiple SQS queues subscribed, which is not possible when using a direct notification configuration.</p>

<p>Here are some sample commands that create an SQS queue and connect it to the SNS topic.</p>

<p>Create the SQS queue and get the ARN (Amazon Resource Name). Some APIs need the SQS URL and some need the SQS ARN. I don&#8217;t know why.</p>

<pre><code>sqs_queue_url=$(aws sqs create-queue   --queue-name $sqs_queue_name   --attributes 'ReceiveMessageWaitTimeSeconds=20,VisibilityTimeout=300'    --output text   --query 'QueueUrl')
echo sqs_queue_url=$sqs_queue_url

sqs_queue_arn=$(aws sqs get-queue-attributes   --queue-url "$sqs_queue_url"   --attribute-names QueueArn   --output text   --query 'Attributes.QueueArn')
echo sqs_queue_arn=$sqs_queue_arn
</code></pre>

<p>Give the SNS topic permission to post to the SQS queue.</p>

<pre><code>sqs_policy='{
    "Version":"2012-10-17",
    "Statement":[
      {
        "Effect":"Allow",
        "Principal": { "AWS": "*" },
        "Action":"sqs:SendMessage",
        "Resource":"'$sqs_queue_arn'",
        "Condition":{
          "ArnEquals":{
            "aws:SourceArn":"'$sns_topic_arn'"
          }
        }
      }
    ]
  }'
sqs_policy_escaped=$(echo $sqs_policy | perl -pe 's/"/\\"/g')
sqs_attributes='{"Policy":"'$sqs_policy_escaped'"}'
aws sqs set-queue-attributes   --queue-url "$sqs_queue_url"   --attributes "$sqs_attributes"
</code></pre>

<p>Subscribe the SQS queue to the SNS topic.</p>

<pre><code>aws sns subscribe   --topic-arn "$sns_topic_arn"   --protocol sqs   --notification-endpoint "$sqs_queue_arn"
</code></pre>

<p>You can upload another test file to the S3 bucket, which will now generate both the email and a message to the SQS queue.</p>

<pre><code>aws s3 cp [SOMEFILE] s3://$s3_bucket_name/testfile-02
</code></pre>

<p>Read the S3 bucket notification message from the SQS queue:</p>

<pre><code>aws sqs receive-message   --queue-url $sqs_queue_url
</code></pre>

<p>The output of that command is not quite human readable as it has quoted JSON inside quoted JSON inside JSON, but your queue processing software should be able to decode it and take appropriate actions.</p>

<p>You can tell the SQS queue that you have &#8220;processed&#8221; the message by grabbing the &#8220;ReceiptHandle&#8221; value from the above output and deleting the message.</p>

<pre><code>sqs_receipt_handle=...
aws sqs delete-message   --queue-url "$sqs_queue_url"   --receipt-handle "$sqs_receipt_handle"
</code></pre>

<p>You only have a limited amount of time to process the message and delete it before SQS tosses it back in the queue for somebody else to process. This test queue gives you 5 minutes (VisibilityTimeout=300). If you go past this timeout, simply read the message from the queue and try again.</p>

<h2>Cleanup</h2>

<p>Delete the SQS queue:</p>

<pre><code>aws sqs delete-queue   --queue-url "$sqs_queue_url"
</code></pre>

<p>Delete the SNS topic (and all subscriptions).</p>

<pre><code>aws sns delete-topic   --region "$region"   --topic-arn "$sns_topic_arn"
</code></pre>

<p>Delete test objects in the bucket:</p>

<pre><code>aws s3 rm s3://$s3_bucket_name/testfile-01
aws s3 rm s3://$s3_bucket_name/testfile-02
</code></pre>

<p>Remove the S3 bucket notification configuration:</p>

<pre><code>aws s3api put-bucket-notification   --region "$region"   --bucket "$s3_bucket   --notification-configuration '{}'
</code></pre>

<p>Delete the bucket, but only if it was created for this test!</p>

<pre><code>aws s3 rb s3://$s3_bucket_name
</code></pre>

<h2>History / Future</h2>

<p>If the concept of an S3 bucket notification sounds a bit familiar, it&#8217;s because AWS S3 has had it for years, but the only supported event type was &#8220;s3:ReducedRedundancyLostObject&#8221;, triggered when S3 lost an RRS object. Given the way that this feature was designed, we all assumed that Amazon would eventually add more useful events like &#8220;S3 object created&#8221;,  which indeed they released a couple weeks ago.</p>

<p>I would continue to assume/hope that Amazon will eventually support an &#8220;S3 object deleted&#8221; event because it just makes too much sense for applications that need to keep track of the keys in a bucket.</p>

<p><em>[Update 2015-04-06: Add code to remove S3 bucket notification, which Amazon just added to aws-cli in release 18]</em></p>

        </div>



    </div>
    <div class="asset-footer"></div>
</div>

    <!--
<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
         xmlns:trackback="http://madskills.com/public/xml/rss/module/trackback/"
         xmlns:dc="http://purl.org/dc/elements/1.1/">
<rdf:Description
    rdf:about="http://alestic.com/2014/11/aws-lambda-speed"
    trackback:ping="http://alestic.com/mt/mt-tb.cgi/160"
    dc:title="AWS Lambda: Pay The Same Price For Faster Execution"
    dc:identifier="http://alestic.com/2014/11/aws-lambda-speed"
    dc:subject="Lambda"
    dc:description="multiply the speed of compute-intensive Lambda functions without (much) increase in cost Given: AWS Lambda duration charges are proportional to the requested memory. The CPU power, network, and disk are proportional to the requested memory. One could conclude that the..."
    dc:creator="Eric Hammond"
    dc:date="2014-11-19T08:00:00-08:00" />
</rdf:RDF>
-->

<div id="entry-172" class="entry-asset asset hentry">
    <div class="asset-header">
        <h2 class="asset-name entry-title"><a href="http://alestic.com/2014/11/aws-lambda-speed" rel="bookmark">AWS Lambda: Pay The Same Price For Faster Execution</a>
        <!-- Google +1 -->
<!-- 
        <g:plusone size="medium" href="http://alestic.com/2014/11/aws-lambda-speed"></g:plusone>
-->
        </h2>
        <div class="asset-meta">
    <span class="byline">

        By <span class="vcard author"><a rel="author" href="https://plus.google.com/111045584683584396225/about" class="fn url">Eric Hammond</a></span> on <abbr class="published" title="2014-11-19T08:00:00-08:00">November 19, 2014  8:00 AM</abbr>

    </span>

    <span class="separator">|</span> <a href="http://alestic.com/2014/11/aws-lambda-speed#comments">0 Comments</a>
<!--
    <span class="separator">|</span> <a href="http://alestic.com/2014/11/aws-lambda-speed#trackbacks">0 TrackBacks</a>
-->

</div>

    </div>
    <div class="asset-content entry-content">

        <div class="asset-body">
            <p><em>multiply the speed of compute-intensive Lambda functions without (much) increase in cost</em></p>

<p>Given:</p>

<ul>
<li><p>AWS Lambda duration charges are proportional to the requested memory.</p></li>
<li><p>The CPU power, network, and disk are proportional to the requested memory.</p></li>
</ul>

<p>One could conclude that the charges are proportional to the CPU power
available to the Lambda function. If the function completion time is
inversely proportional to the CPU power allocated (not entirely true),
then the cost remains roughly fixed as you dial up power to make it
faster.</p>

<p>If your Lambda function is primarily CPU bound and takes at least
several hundred ms to execute, then you may find that you can simply
allocate more CPU by allocating more memory, and get the same
functionality completed in a shorter time period for about the same
cost.</p>

<p>For example, if you allocate 128 MB of memory and your Lambda function
takes 10 seconds to run, then you might be able to allocate 640 MB and
see it complete in about 2 seconds.</p>

<p>At current AWS Lambda pricing, both of these would cost about $0.02
per thousand invocations, but the second one completes five times
faster.</p>

<p>Things that would cause the higher memory/CPU option to cost more in total
include:</p>

<ul>
<li><p>Time chunks are rounded up to the nearest 100 ms.  If your Lambda
function runs near or under that in less memory, then increasing
the CPU allocated will make it return faster, but the rounding up
will cause the resulting cost to be more expensive.</p></li>
<li><p>Doubling the CPU allocated to a Lambda function does not
necessarily cut the run time in half. The code might be accessing
external resources (e.g., calling S3 APIs) or interacting with
disk. If you double the requested CPU, then those fixed time
actions will end up costing twice as much.</p></li>
</ul>

<p>If you have a slow Lambda function, and it seems that most of its time
is probably spent in CPU activities, then it might be worth testing an
increase in requested memory to see if you can get it to complete
much faster without increasing the cost by much.</p>

<p>I&#8217;d love to hear what practical test results people find when
comparing different memory/CPU allocation values for the same Lambda
function.</p>

        </div>



    </div>
    <div class="asset-footer"></div>
</div>

    <!--
<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
         xmlns:trackback="http://madskills.com/public/xml/rss/module/trackback/"
         xmlns:dc="http://purl.org/dc/elements/1.1/">
<rdf:Description
    rdf:about="http://alestic.com/2014/11/aws-lambda-environment"
    trackback:ping="http://alestic.com/mt/mt-tb.cgi/162"
    dc:title="Exploring The AWS Lambda Runtime Environment"
    dc:identifier="http://alestic.com/2014/11/aws-lambda-environment"
    dc:subject="Lambda"
    dc:description="In the AWS Lambda Shell Hack article, I present a crude hack that lets me run shell commands in the AWS Lambda environment to explore what might be available to Lambda functions running there. I&#8217;ve added a wrapper that lets..."
    dc:creator="Eric Hammond"
    dc:date="2014-11-18T16:00:00-08:00" />
</rdf:RDF>
-->

<div id="entry-174" class="entry-asset asset hentry">
    <div class="asset-header">
        <h2 class="asset-name entry-title"><a href="http://alestic.com/2014/11/aws-lambda-environment" rel="bookmark">Exploring The AWS Lambda Runtime Environment</a>
        <!-- Google +1 -->
<!-- 
        <g:plusone size="medium" href="http://alestic.com/2014/11/aws-lambda-environment"></g:plusone>
-->
        </h2>
        <div class="asset-meta">
    <span class="byline">

        By <span class="vcard author"><a rel="author" href="https://plus.google.com/111045584683584396225/about" class="fn url">Eric Hammond</a></span> on <abbr class="published" title="2014-11-18T16:00:00-08:00">November 18, 2014  4:00 PM</abbr>

    </span>

    <span class="separator">|</span> <a href="http://alestic.com/2014/11/aws-lambda-environment#comments">4 Comments</a>
<!--
    <span class="separator">|</span> <a href="http://alestic.com/2014/11/aws-lambda-environment#trackbacks">0 TrackBacks</a>
-->

</div>

    </div>
    <div class="asset-content entry-content">

        <div class="asset-body">
            <p>In the <a href="http://alestic.com/2014/11/aws-lambda-shell">AWS Lambda Shell Hack</a> article, I present a crude hack that lets me run shell commands in the AWS Lambda environment to explore what might be available to Lambda functions running there.</p>

<p>I&#8217;ve added a wrapper that lets me type commands on my laptop and see the output of the command run in the Lambda function. This is not production quality software, but you can take a look at it in the <a href="https://github.com/alestic/lambdash">alestic/lambdash GitHub repo</a>.</p>

<p>For the curious, here are some results. Please note that this is running on a preview and is in no way a guaranteed part of the environment of a Lambda function. Amazon could change any of it at any time, so don&#8217;t build production code using this information.</p>

<p>The version of Amazon Linux:</p>

<pre><code>$ lambdash cat /etc/issue
Amazon Linux AMI release 2014.03
Kernel \r on an \m
</code></pre>

<p>The kernel version:</p>

<pre><code>$ lambdash uname -a
Linux ip-10-0-168-157 3.14.19-17.43.amzn1.x86_64 #1 SMP Wed Sep 17 22:14:52 UTC 2014 x86_64 x86_64 x86_64 GNU/Linux
</code></pre>

<p>The working directory of the Lambda function:</p>

<pre><code>$ lambdash pwd
/var/task
</code></pre>

<p>which contains the unzipped contents of the Lambda function I uploaded:</p>

<pre><code>$ lambdash ls -l
total 12
-rw-rw-r-- 1 slicer 497 5195 Nov 18 05:52 lambdash.js
drwxrwxr-x 5 slicer 497 4096 Nov 18 05:52 node_modules
</code></pre>

<p>The user running the Lambda function:</p>

<pre><code>$ lambdash id
uid=495(sbx_user1052) gid=494 groups=494
</code></pre>

<p>which is one of one hundred <code>sbx_userNNNN</code> users in <code>/etc/passwd</code>. &#8220;<code>sbx_user</code>&#8221; presumably stands for &#8220;sandbox user&#8221;.</p>

<p>The environment variables (in a shell subprocess). This appears to be how AWS Lambda is passing the AWS credentials to the Lambda function.</p>

<pre><code>$ lambdash env
 AWS_SESSION_TOKEN=[ELIDED]
LAMBDA_TASK_ROOT=/var/task
LAMBDA_CONSOLE_SOCKET=14
PATH=/usr/local/bin:/usr/bin:/bin
PWD=/var/task
AWS_SECRET_ACCESS_KEY=[ELIDED]
NODE_PATH=/var/runtime:/var/task:/var/runtime/node_modules
AWS_ACCESS_KEY_ID=[ELIDED]
SHLVL=1
LAMBDA_CONTROL_SOCKET=11
_=/usr/bin/env
</code></pre>

<p>The versions of various pre-installed software:</p>

<pre><code>$ lambdash perl -v
This is perl 5, version 16, subversion 3 (v5.16.3) built for x86_64-linux-thread-multi
[...]

$ lambdash python --version
Python 2.6.9

$ lambdash node -v
v0.10.32
</code></pre>

<p>Running processes:</p>

<pre><code>$ lambdash ps axu
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
493          1  0.2  0.7 1035300 27080 ?       Ssl  14:26   0:00 node --max-old-space-size=0 --max-new-space-size=0 --max-executable-size=0 /var/runtime/node_modules/.bin/awslambda
493         13  0.0  0.0  13444  1084 ?        R    14:29   0:00 ps axu
</code></pre>

<p>The entire file system: <a href="http://s3.alestic.com/archive/aws-lambda-ls-laiR-20141117.txt">2.5 MB download</a></p>

<pre><code> $ lambdash ls -laiR /
 [click link above to download]
</code></pre>

<p>Kernel ring buffer: <a href="http://s3.alestic.com/archive/aws-lambda-dmesg-20141118.txt">34K download</a></p>

<pre><code>$ lambdash dmesg
[click link above to download]
</code></pre>

<p>CPU info:</p>

<pre><code>$ lambdash cat /proc/cpuinfo
processor   : 0
vendor_id   : GenuineIntel
cpu family  : 6
model       : 62
model name  : Intel(R) Xeon(R) CPU E5-2680 v2 @ 2.80GHz
stepping    : 4
microcode   : 0x416
cpu MHz     : 2800.110
cache size  : 25600 KB
physical id : 0
siblings    : 2
core id     : 0
cpu cores   : 1
apicid      : 0
initial apicid  : 0
fpu     : yes
fpu_exception   : yes
cpuid level : 13
wp      : yes
flags       : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx rdtscp lm constant_tsc rep_good nopl xtopology eagerfpu pni pclmulqdq ssse3 cx16 pcid sse4_1 sse4_2 x2apic popcnt tsc_deadline_timer aes xsave avx f16c rdrand hypervisor lahf_lm xsaveopt fsgsbase smep erms
bogomips    : 5600.22
clflush size    : 64
cache_alignment : 64
address sizes   : 46 bits physical, 48 bits virtual
power management:

processor   : 1
vendor_id   : GenuineIntel
[...]
</code></pre>

<p>Installed nodejs modules:</p>

<pre><code>$ dirs=$(lambdash 'echo $NODE_PATH' | tr ':' '\n' | sort)
$ echo $dirs
/var/runtime /var/runtime/node_modules /var/task

$ lambdash 'for dir in '$dirs'; do echo $dir; ls -1 $dir; echo; done'
/var/runtime
node_modules

/var/runtime/node_modules
aws-sdk
awslambda
dynamodb-doc
imagemagick

/var/task # Uploaded in Lambda function ZIP file
lambdash.js
node_modules
</code></pre>

<p><em>[Update 2013-12-03]</em></p>

<p>We&#8217;re probably not on a bare EC2 instance. The standard EC2 instance metadata service is not accessible through HTTP:</p>

<pre><code>$ lambdash curl -sS http://169.254.169.254:8000/latest/meta-data/instance-type
curl: (7) Failed to connect to 169.254.169.254 port 8000: Connection refused
</code></pre>

<p>Browsing the AWS Lambda environment source code turns up some nice hints about where the product might be heading. I won&#8217;t paste the copyrighted code here, but you can download into an &#8220;awslambda&#8221; subdirectory with:</p>

<pre><code>$ lambdash 'cd /var/runtime/node_modules;tar c awslambda' | tar xv
</code></pre>

<p><em>[Update 2013-12-11]</em></p>

<p>There&#8217;s a half gig of writable disk space available under /tmp (when run with 256MB of RAM. Does this scale up with memory?)</p>

<pre><code>$ lambdash 'df -h 2&gt;/dev/null'
Filesystem      Size  Used Avail Use% Mounted on
/dev/xvda1       30G  1.9G   28G   7% /
devtmpfs         30G  1.9G   28G   7% /dev
/dev/xvda1       30G  1.9G   28G   7% /
/dev/loop0      526M  832K  514M   1% /tmp
</code></pre>

<p>Anything else you&#8217;d like to see? Suggest commands in the comments on this article.</p>

        </div>



    </div>
    <div class="asset-footer"></div>
</div>

    <!--
<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
         xmlns:trackback="http://madskills.com/public/xml/rss/module/trackback/"
         xmlns:dc="http://purl.org/dc/elements/1.1/">
<rdf:Description
    rdf:about="http://alestic.com/2014/11/aws-lambda-shell"
    trackback:ping="http://alestic.com/mt/mt-tb.cgi/161"
    dc:title="lambdash: AWS Lambda Shell Hack"
    dc:identifier="http://alestic.com/2014/11/aws-lambda-shell"
    dc:subject="Lambda"
    dc:description="I spent the weekend learning just enough JavaScript and nodejs to hack together a Lambda function that runs arbitrary shell commands in the AWS Lambda environment. This hack allows you to explore the current file system, learn what versions of..."
    dc:creator="Eric Hammond"
    dc:date="2014-11-18T09:00:00-08:00" />
</rdf:RDF>
-->

<div id="entry-173" class="entry-asset asset hentry">
    <div class="asset-header">
        <h2 class="asset-name entry-title"><a href="http://alestic.com/2014/11/aws-lambda-shell" rel="bookmark">lambdash: AWS Lambda Shell Hack</a>
        <!-- Google +1 -->
<!-- 
        <g:plusone size="medium" href="http://alestic.com/2014/11/aws-lambda-shell"></g:plusone>
-->
        </h2>
        <div class="asset-meta">
    <span class="byline">

        By <span class="vcard author"><a rel="author" href="https://plus.google.com/111045584683584396225/about" class="fn url">Eric Hammond</a></span> on <abbr class="published" title="2014-11-18T09:00:00-08:00">November 18, 2014  9:00 AM</abbr>

    </span>

    <span class="separator">|</span> <a href="http://alestic.com/2014/11/aws-lambda-shell#comments">0 Comments</a>
<!--
    <span class="separator">|</span> <a href="http://alestic.com/2014/11/aws-lambda-shell#trackbacks">1 TrackBack</a>
-->

</div>

    </div>
    <div class="asset-content entry-content">

        <div class="asset-body">
            <p>I spent the weekend learning just enough JavaScript and nodejs to hack
together a <a href="https://github.com/alestic/lambdash">Lambda function that runs arbitrary shell commands in the
AWS Lambda environment</a>.</p>

<p>This hack allows you to explore the current file system, learn what
versions of Perl and Python are available, and discover what
packages might be installed.</p>

<p>If you&#8217;re interested in seeing the results, then read following article which uses this AWS Lambda shell hack to examine the inside of the AWS Lambda run time environment.</p>

<blockquote>
  <p><a href="http://alestic.com/2014/11/aws-lambda-environment">Exploring The AWS Lambda Runtime Environment</a></p>
</blockquote>

<p>Now on to the hack&#8230;</p>

<h2>Setup</h2>

<p>Define the basic parameters.</p>

<pre><code># Replace with your bucket name
bucket_name=lambdash.alestic.com

function=lambdash
lambda_execution_role_name=lambda-$function-execution
lambda_execution_access_policy_name=lambda-$function-execution-access
log_group_name=/aws/lambda/$function
</code></pre>

<p>IAM role that will be used by the Lambda function when it runs.</p>

<pre><code>lambda_execution_role_arn=$(aws iam create-role   --role-name "$lambda_execution_role_name"   --assume-role-policy-document '{
      "Version": "2012-10-17",
      "Statement": [{
          "Sid": "",
          "Effect": "Allow",
          "Principal": {
            "Service": "lambda.amazonaws.com"
          },
          "Action": "sts:AssumeRole"
      }]
    }'   --output text   --query 'Role.Arn'
)
echo lambda_execution_role_arn=$lambda_execution_role_arn
</code></pre>

<p>What the Lambda function is allowed to do/access. Log to Cloudwatch
and upload files to a specific S3 bucket/location.</p>

<pre><code>aws iam put-role-policy   --role-name "$lambda_execution_role_name"   --policy-name "$lambda_execution_access_policy_name"   --policy-document '{
      "Version": "2012-10-17",
      "Statement": [{
          "Effect": "Allow",
          "Action": [ "logs:*" ],
          "Resource": "arn:aws:logs:*:*:*"
      }, {
          "Effect": "Allow",
          "Action": [ "s3:PutObject" ],
          "Resource": "arn:aws:s3:::'$bucket_name'/'$function'/*"
      }]
  }'
</code></pre>

<p>Grab the current Lambda function JavaScript from the <a href="https://github.com/alestic/lambdash">Alestic lambdash
GitHub repository</a>, create the ZIP file, and upload the new
Lambda function.</p>

<pre><code>wget -q -O$function.js   https://raw.githubusercontent.com/alestic/lambdash/master/lambdash.js
npm install async fs tmp
zip -r $function.zip $function.js node_modules
aws lambda upload-function   --function-name "$function"   --function-zip "$function.zip"   --runtime nodejs   --mode event   --handler "$function.handler"   --role "$lambda_execution_role_arn"   --timeout 60   --memory-size 256
</code></pre>

<p>Invoke the Lambda function with the desired command and S3 output
locations. Adjust the command and repeat as desired.</p>

<pre><code>cat &gt; $function-args.json &lt;&lt;EOM
{
    "command": "ls -laiR /",
    "bucket":  "$bucket_name",
    "stdout":  "$function/stdout.txt",
    "stderr":  "$function/stderr.txt"
}
EOM

aws lambda invoke-async   --function-name "$function"   --invoke-args "$function-args.json"
</code></pre>

<p>Look at the Lambda function log output in CloudWatch.</p>

<pre><code>log_stream_names=$(aws logs describe-log-streams   --log-group-name "$log_group_name"   --output text   --query 'logStreams[*].logStreamName') &amp;&amp;
for log_stream_name in $log_stream_names; do
  aws logs get-log-events     --log-group-name "$log_group_name"     --log-stream-name "$log_stream_name"     --output text     --query 'events[*].message'
done | less
</code></pre>

<p>Get the command output.</p>

<pre><code>aws s3 cp s3://$bucket_name/$function/stdout.txt .
aws s3 cp s3://$bucket_name/$function/stderr.txt .
less stdout.txt stderr.txt
</code></pre>

<h2>Clean up</h2>

<p>If you are done with this example, you can delete the created
resources. Or, you can leave the Lambda function in place ready for
future use. After all, you aren&#8217;t charged unless you use it.</p>

<pre><code>aws s3 rm s3://$bucket_name/$function/stdout.txt
aws s3 rm s3://$bucket_name/$function/stderr.txt
aws lambda delete-function   --function-name "$function"
aws iam delete-role-policy   --role-name "$lambda_execution_role_name"   --policy-name "$lambda_execution_access_policy_name"
aws iam delete-role   --role-name "$lambda_execution_role_name"
aws logs delete-log-group   --log-group-name "$log_group_name"
</code></pre>

<h2>Requests</h2>

<p>What command output would you like to see in the Lambda environment?</p>

        </div>



    </div>
    <div class="asset-footer"></div>
</div>

    <!--
<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
         xmlns:trackback="http://madskills.com/public/xml/rss/module/trackback/"
         xmlns:dc="http://purl.org/dc/elements/1.1/">
<rdf:Description
    rdf:about="http://alestic.com/2014/11/aws-lambda-cli"
    trackback:ping="http://alestic.com/mt/mt-tb.cgi/159"
    dc:title="AWS Lambda Walkthrough Command Line Companion"
    dc:identifier="http://alestic.com/2014/11/aws-lambda-cli"
    dc:subject="PlanetUbuntu"
    dc:description="The AWS Lambda Walkthrough 2 uses AWS Lambda to automatically resize images added to one bucket, placing the resulting thumbnails in another bucket. The walkthrough documentation has a mix of aws-cli commands, instructions for hand editing files, and steps requiring..."
    dc:creator="Eric Hammond"
    dc:date="2014-11-14T11:11:11-08:00" />
</rdf:RDF>
-->

<div id="entry-171" class="entry-asset asset hentry">
    <div class="asset-header">
        <h2 class="asset-name entry-title"><a href="http://alestic.com/2014/11/aws-lambda-cli" rel="bookmark">AWS Lambda Walkthrough Command Line Companion</a>
        <!-- Google +1 -->
<!-- 
        <g:plusone size="medium" href="http://alestic.com/2014/11/aws-lambda-cli"></g:plusone>
-->
        </h2>
        <div class="asset-meta">
    <span class="byline">

        By <span class="vcard author"><a rel="author" href="https://plus.google.com/111045584683584396225/about" class="fn url">Eric Hammond</a></span> on <abbr class="published" title="2014-11-14T11:11:11-08:00">November 14, 2014 11:11 AM</abbr>

    </span>

    <span class="separator">|</span> <a href="http://alestic.com/2014/11/aws-lambda-cli#comments">0 Comments</a>
<!--
    <span class="separator">|</span> <a href="http://alestic.com/2014/11/aws-lambda-cli#trackbacks">0 TrackBacks</a>
-->

</div>

    </div>
    <div class="asset-content entry-content">

        <div class="asset-body">
            <p>The <a href="http://docs.aws.amazon.com/lambda/latest/dg/walkthrough-s3-events-adminuser.html">AWS Lambda Walkthrough 2</a> uses <a href="http://aws.amazon.com/lambda/">AWS Lambda</a> to
automatically resize images added to one bucket, placing the resulting
thumbnails in another bucket. The walkthrough documentation has a mix
of aws-cli commands, instructions for hand editing files, and steps
requiring the AWS console.</p>

<p>For my personal testing, I converted all of these to command line
instructions that can simply be copied and pasted, making them more
suitable for adapting into scripts and for eventual automation. I
share the results here in case others might find this a faster way to
get started with Lambda.</p>

<p>These instructions assume that you have already set up and are using
an IAM user / aws-cli profile with admin credentials.</p>

<p>The following is intended as a companion to the Amazon walkthrough
documentation, simplifying the execution steps for command line
lovers. Read the <a href="http://docs.aws.amazon.com/lambda/latest/dg/walkthrough-s3-events-adminuser.html">AWS documentation</a> itself for more
details explaining the walkthrough.</p>

<h2>Set up</h2>

<p>Set up environment variables describing the associated resources:</p>

<pre><code># Change to your own unique S3 bucket name:
source_bucket=alestic-lambda-example

# Do not change this. Walkthrough code assumes this name
target_bucket=${source_bucket}resized

function=CreateThumbnail
lambda_execution_role_name=lambda-$function-execution
lambda_execution_access_policy_name=lambda-$function-execution-access
lambda_invocation_role_name=lambda-$function-invocation
lambda_invocation_access_policy_name=lambda-$function-invocation-access
log_group_name=/aws/lambda/$function
</code></pre>

<p>Install some required software:</p>

<pre><code>sudo apt-get install nodejs nodejs-legacy npm
</code></pre>

<h2>Step 1.1: Create Buckets and Upload a Sample Object (<a href="http://docs.aws.amazon.com/lambda/latest/dg/walkthrough-s3-events-adminuser-prepare.html">walkthrough</a>)</h2>

<p>Create the buckets:</p>

<pre><code>aws s3 mb s3://$source_bucket
aws s3 mb s3://$target_bucket
</code></pre>

<p>Upload a sample photo:</p>

<pre><code># by Hatalmas: https://www.flickr.com/photos/hatalmas/6094281702
wget -q -OHappyFace.jpg   https://c3.staticflickr.com/7/6209/6094281702_d4ac7290d3_b.jpg

aws s3 cp HappyFace.jpg s3://$source_bucket/
</code></pre>

<h2>Step 2.1: Create a Lambda Function Deployment Package (<a href="http://docs.aws.amazon.com/lambda/latest/dg/walkthrough-s3-events-adminuser-create-test-function-create-function.html">walkthrough</a>)</h2>

<p>Create the Lambda function nodejs code:</p>

<pre><code># JavaScript code as listed in walkthrough
wget -q -O $function.js   http://run.alestic.com/lambda/aws-examples/CreateThumbnail.js
</code></pre>

<p>Install packages needed by the Lambda function code. Note that this is
done under the local directory:</p>

<pre><code>npm install async gm # aws-sdk is not needed
</code></pre>

<p>Put all of the required code into a ZIP file, ready for uploading:</p>

<pre><code>zip -r $function.zip $function.js node_modules
</code></pre>

<h2>Step 2.2: Create an IAM Role for AWS Lambda (<a href="http://docs.aws.amazon.com/lambda/latest/dg/walkthrough-s3-events-adminuser-create-test-function-create-execution-role.html">walkthrough</a>)</h2>

<p>IAM role that will be used by the Lambda function when it runs.</p>

<pre><code>lambda_execution_role_arn=$(aws iam create-role   --role-name "$lambda_execution_role_name"   --assume-role-policy-document '{
      "Version": "2012-10-17",
      "Statement": [
        {
          "Sid": "",
          "Effect": "Allow",
          "Principal": {
            "Service": "lambda.amazonaws.com"
          },
          "Action": "sts:AssumeRole"
        }
      ]
    }'   --output text   --query 'Role.Arn'
)
echo lambda_execution_role_arn=$lambda_execution_role_arn
</code></pre>

<p>What the Lambda function is allowed to do/access. This is slightly
tighter than the generic role policy created with the IAM console:</p>

<pre><code>aws iam put-role-policy   --role-name "$lambda_execution_role_name"   --policy-name "$lambda_execution_access_policy_name"   --policy-document '{
    "Version": "2012-10-17",
    "Statement": [
      {
        "Effect": "Allow",
        "Action": [
          "logs:*"
        ],
        "Resource": "arn:aws:logs:*:*:*"
      },
      {
        "Effect": "Allow",
        "Action": [
          "s3:GetObject"
        ],
        "Resource": "arn:aws:s3:::'$source_bucket'/*"
      },
      {
        "Effect": "Allow",
        "Action": [
          "s3:PutObject"
        ],
        "Resource": "arn:aws:s3:::'$target_bucket'/*"
      }
    ]
  }'
</code></pre>

<h2>Step 2.3: Upload the Deployment Package and Invoke it Manually (<a href="http://docs.aws.amazon.com/lambda/latest/dg/walkthrough-s3-events-adminuser-create-test-function-upload-zip-test.html">walkthrough</a>)</h2>

<p>Upload the Lambda function, specifying the IAM role it should use and
other attributes:</p>

<pre><code># Timeout increased from walkthrough based on experience
aws lambda upload-function   --function-name "$function"   --function-zip "$function.zip"   --role "$lambda_execution_role_arn"   --mode event   --handler "$function.handler"   --timeout 30   --runtime nodejs
</code></pre>

<p>Create fake S3 event data to pass to the Lambda function. The key here is
the source S3 bucket and key:</p>

<pre><code>cat &gt; $function-data.json &lt;&lt;EOM
{  
   "Records":[  
      {  
         "eventVersion":"2.0",
         "eventSource":"aws:s3",
         "awsRegion":"us-east-1",
         "eventTime":"1970-01-01T00:00:00.000Z",
         "eventName":"ObjectCreated:Put",
         "userIdentity":{  
            "principalId":"AIDAJDPLRKLG7UEXAMPLE"
         },
         "requestParameters":{  
            "sourceIPAddress":"127.0.0.1"
         },
         "responseElements":{  
            "x-amz-request-id":"C3D13FE58DE4C810",
            "x-amz-id-2":"FMyUVURIY8/IgAtTv8xRjskZQpcIZ9KG4V5Wp6S7S/JRWeUWerMUE5JgHvANOjpD"
         },
         "s3":{  
            "s3SchemaVersion":"1.0",
            "configurationId":"testConfigRule",
            "bucket":{  
               "name":"$source_bucket",
               "ownerIdentity":{  
                  "principalId":"A3NL1KOZZKExample"
               },
               "arn":"arn:aws:s3:::$source_bucket"
            },
            "object":{  
               "key":"HappyFace.jpg",
               "size":1024,
               "eTag":"d41d8cd98f00b204e9800998ecf8427e",
               "versionId":"096fKKXTRTtl3on89fVO.nfljtsv6qko"
            }
         }
      }
   ]
}
EOM
</code></pre>

<p>Invoke the Lambda function, passing in the fake S3 event data:</p>

<pre><code>aws lambda invoke-async   --function-name "$function"   --invoke-args "$function-data.json"
</code></pre>

<p>Look in the target bucket for the converted image. It could take a
while to show up since the Lambda function is running asynchronously:</p>

<pre><code>aws s3 ls s3://$target_bucket
</code></pre>

<p>Look at the Lambda function log output in CloudWatch:</p>

<pre><code>aws logs describe-log-groups   --output text   --query 'logGroups[*].[logGroupName]'

log_stream_names=$(aws logs describe-log-streams   --log-group-name "$log_group_name"   --output text   --query 'logStreams[*].logStreamName')
echo log_stream_names="'$log_stream_names'"
for log_stream_name in $log_stream_names; do
  aws logs get-log-events     --log-group-name "$log_group_name"     --log-stream-name "$log_stream_name"     --output text     --query 'events[*].message'
done | less
</code></pre>

<h2>Step 3.1: Create an IAM Role for Amazon S3 (<a href="http://docs.aws.amazon.com/lambda/latest/dg/walkthrough-s3-events-adminuser-create-invocationrole-grant-user-passrole.html">walkthrough</a>)</h2>

<p>This role may be assumed by S3.</p>

<pre><code>lambda_invocation_role_arn=$(aws iam create-role   --role-name "$lambda_invocation_role_name"   --assume-role-policy-document '{
      "Version": "2012-10-17",
      "Statement": [
        {
          "Sid": "",
          "Effect": "Allow",
          "Principal": {
            "Service": "s3.amazonaws.com"
          },
          "Action": "sts:AssumeRole",
          "Condition": {
            "StringLike": {
              "sts:ExternalId": "arn:aws:s3:::*"
            }
          }
        }
      ]
    }'   --output text   --query 'Role.Arn'
)
echo lambda_invocation_role_arn=$lambda_invocation_role_arn
</code></pre>

<p>S3 may invoke the Lambda function.</p>

<pre><code>aws iam put-role-policy   --role-name "$lambda_invocation_role_name"   --policy-name "$lambda_invocation_access_policy_name"   --policy-document '{
     "Version": "2012-10-17",
     "Statement": [
       {
         "Effect": "Allow",
         "Action": [
           "lambda:InvokeFunction"
         ],
         "Resource": [
           "*"
         ]
       }
     ]
   }'
</code></pre>

<h2>Step 3.2: Configure a Notification on the Bucket (<a href="http://docs.aws.amazon.com/lambda/latest/dg/walkthrough-s3-events-adminuser-attach-notification-configuration.html">walkthrough</a>)</h2>

<p>Get the Lambda function ARN:</p>

<pre><code>lambda_function_arn=$(aws lambda get-function-configuration   --function-name "$function"   --output text   --query 'FunctionARN'
)
echo lambda_function_arn=$lambda_function_arn
</code></pre>

<p>Tell the S3 bucket to invoke the Lambda function when new objects are
created (or overwritten):</p>

<pre><code>aws s3api put-bucket-notification   --bucket "$source_bucket"   --notification-configuration '{
    "CloudFunctionConfiguration": {
      "CloudFunction": "'$lambda_function_arn'",
      "InvocationRole": "'$lambda_invocation_role_arn'",
      "Event": "s3:ObjectCreated:*"
    }
  }'
</code></pre>

<h2>Step 3.3: Test the Setup (<a href="http://docs.aws.amazon.com/lambda/latest/dg/walkthrough-s3-final-integration-test-no-iam.html">walkthrough</a>)</h2>

<p>Copy your own jpg and png files into the source bucket:</p>

<pre><code>myimages=...
aws s3 cp $myimages s3://$source_bucket/
</code></pre>

<p>Look for the resized images in the target bucket:</p>

<pre><code>aws s3 ls s3://$target_bucket
</code></pre>

<h2>Check out the environment</h2>

<p>These handy commands let you review the related resources in your acccount:</p>

<pre><code>aws lambda list-functions   --output text   --query 'Functions[*].[FunctionName]'

aws lambda get-function   --function-name "$function"

aws iam list-roles   --output text   --query 'Roles[*].[RoleName]'

aws iam get-role   --role-name "$lambda_execution_role_name"   --output json   --query 'Role.AssumeRolePolicyDocument.Statement'

aws iam list-role-policies    --role-name "$lambda_execution_role_name"   --output text   --query 'PolicyNames[*]'

aws iam get-role-policy   --role-name "$lambda_execution_role_name"   --policy-name "$lambda_execution_access_policy_name"   --output json   --query 'PolicyDocument'

aws iam get-role   --role-name "$lambda_invocation_role_name"   --output json   --query 'Role.AssumeRolePolicyDocument.Statement'

aws iam list-role-policies    --role-name "$lambda_invocation_role_name"   --output text   --query 'PolicyNames[*]'

aws iam get-role-policy   --role-name "$lambda_invocation_role_name"   --policy-name "$lambda_invocation_access_policy_name"   --output json   --query 'PolicyDocument'

aws s3api get-bucket-notification   --bucket "$source_bucket"
</code></pre>

<h2>Clean up</h2>

<p>If you are done with the walkthrough, you can delete the created resources:</p>

<pre><code>aws s3 rm s3://$target_bucket/resized-HappyFace.jpg
aws s3 rm s3://$source_bucket/HappyFace.jpg
aws s3 rb s3://$target_bucket/
aws s3 rb s3://$source_bucket/

aws lambda delete-function   --function-name "$function"

aws iam delete-role-policy   --role-name "$lambda_execution_role_name"   --policy-name "$lambda_execution_access_policy_name"

aws iam delete-role   --role-name "$lambda_execution_role_name"

aws iam delete-role-policy   --role-name "$lambda_invocation_role_name"   --policy-name "$lambda_invocation_access_policy_name"

aws iam delete-role   --role-name "$lambda_invocation_role_name"

log_stream_names=$(aws logs describe-log-streams   --log-group-name "$log_group_name"   --output text   --query 'logStreams[*].logStreamName') &amp;&amp;
for log_stream_name in $log_stream_names; do
  echo "deleting log-stream $log_stream_name"
  aws logs delete-log-stream     --log-group-name "$log_group_name"     --log-stream-name "$log_stream_name"
done

aws logs delete-log-group   --log-group-name "$log_group_name"
</code></pre>

<p>If you try these instructions, please let me know in the comments
where you had trouble or experienced errors.</p>

        </div>



    </div>
    <div class="asset-footer"></div>
</div>

    <!--
<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
         xmlns:trackback="http://madskills.com/public/xml/rss/module/trackback/"
         xmlns:dc="http://purl.org/dc/elements/1.1/">
<rdf:Description
    rdf:about="http://alestic.com/2014/11/aws-iam-ssl-certificate-expiration"
    trackback:ping="http://alestic.com/mt/mt-tb.cgi/157"
    dc:title="When Are Your SSL Certificates Expiring on AWS?"
    dc:identifier="http://alestic.com/2014/11/aws-iam-ssl-certificate-expiration"
    dc:subject="CloudFront"
    dc:description="If you uploaded SSL certificates to Amazon Web Services for ELB (Elastic Load Balancing) or CloudFront (CDN), then you will want to keep an eye on the expiration dates and renew the certificates well before to ensure uninterrupted service. If..."
    dc:creator="Eric Hammond"
    dc:date="2014-11-06T06:00:00-08:00" />
</rdf:RDF>
-->

<div id="entry-169" class="entry-asset asset hentry">
    <div class="asset-header">
        <h2 class="asset-name entry-title"><a href="http://alestic.com/2014/11/aws-iam-ssl-certificate-expiration" rel="bookmark">When Are Your SSL Certificates Expiring on AWS?</a>
        <!-- Google +1 -->
<!-- 
        <g:plusone size="medium" href="http://alestic.com/2014/11/aws-iam-ssl-certificate-expiration"></g:plusone>
-->
        </h2>
        <div class="asset-meta">
    <span class="byline">

        By <span class="vcard author"><a rel="author" href="https://plus.google.com/111045584683584396225/about" class="fn url">Eric Hammond</a></span> on <abbr class="published" title="2014-11-06T06:00:00-08:00">November  6, 2014  6:00 AM</abbr>

    </span>

    <span class="separator">|</span> <a href="http://alestic.com/2014/11/aws-iam-ssl-certificate-expiration#comments">0 Comments</a>
<!--
    <span class="separator">|</span> <a href="http://alestic.com/2014/11/aws-iam-ssl-certificate-expiration#trackbacks">0 TrackBacks</a>
-->

</div>

    </div>
    <div class="asset-content entry-content">

        <div class="asset-body">
            <p>If you uploaded SSL certificates to Amazon Web Services for ELB (Elastic Load Balancing) or CloudFront (CDN), then you will want to keep an eye on the expiration dates and renew the certificates well before to ensure uninterrupted service.</p>

<p>If you uploaded the SSL certificates yourself, then of course at that time you set an official reminder to make sure that you remembered to renew the certificate. Right?</p>

<p>However, if you inherited an AWS account and want to review your company or client&#8217;s configuration, then here&#8217;s an easy command to get a list of all SSL certificates in IAM, sorted by expiration date.</p>

<pre><code>aws iam list-server-certificates   --output text   --query 'ServerCertificateMetadataList[*].[Expiration,ServerCertificateName]'   | sort
</code></pre>

<p>To get more information on an individual certificate, you might use something like:</p>

<pre><code>certificate_name=...
aws iam get-server-certificate   --server-certificate-name $certificate_name   --output text   --query 'ServerCertificate.CertificateBody' | openssl x509 -text | less
</code></pre>

<p>That can let you review information like the DNS name(s) the SSL certificate is good for.</p>

<p>Exercise for the reader: Schedule an automated job that reviews SSL certificate expiration and generates messages to an SNS topic when certificates are near expiration. Subscribe email addresses and other alerting services to the SNS topic.</p>

<p>Read more from Amazon on <a href="http://docs.aws.amazon.com/IAM/latest/UserGuide/ManagingServerCerts.html">Managing Server Certificates</a>.</p>

<p>Note: SSL certificates embedded in web server applications running on EC2 instances would have to be checked and updated separately from those stored in AWS.</p>

        </div>



    </div>
    <div class="asset-footer"></div>
</div>


<div class="content-nav">
    <a href="http://alestic.com/archives.html">Archives</a>
</div>

</div>
                    </div>
                <div id="beta">
    <div id="beta-inner">

        <div class="widget-recent-entries widget-archives widget">
<!-- 
    <h3 class="widget-header">Stay Updated</h3>
-->
    <div class="widget-content">
      <dl>
        <dt><a href="http://twitter.com/esh"><img id="optimizely_930317528" src="/img/eric-hammond-2-48x48.jpg" align="right" style="left-margin:10px">Follow Eric Hammond on Twitter</a></dt>

<!-- 
        <dd class="entry-meta"></dd>

        <dt>Subscribe with email address:</dh>
        <dd>
<form action="http://feedburner.google.com/fb/a/mailverify" 
method="post" target="popupwindow" 
onsubmit="window.open('http://feedburner.google.com/fb/a/mailverify?uri=alestic', 'popupwindow', 'scrollbars=yes,width=550,height=520');return true">
<input type="text" style="width:190px" name="email"/>
<input type="hidden" value="alestic" name="uri"/><input type="hidden" name="loc" value="en_US"/>
<input type="submit" value="Subscribe" />
</form>
        </dd>

        <dd class="entry-meta"></dd>

        <dt><a href="http://feeds.alestic.com/alestic" rel="alternate" type="application/rss+xml"><img src="http://www.feedburner.com/fb/images/pub/feed-icon16x16.png" alt="" style="vertical-align:middle;border:0"/></a>&nbsp;<a href="http://feeds2.feedburner.com/alestic" rel="alternate" type="application/rss+xml">Subscribe with a reader</a></dt>
        <dd class="entry-meta"></dd>

        <dt>Join the <a href="http://ec2ubuntu-group.notlong.com">EC2 Ubuntu Google Group</a></dh>

-->

      </dl>
</div>
</div>
<script type="text/javascript">//<![CDATA[
var ON=function(region){
  document.getElementById('ami-comments').style.display        = 'block';


  document.getElementById('tab-us-east-1').style.display       = 
    (region == 'us-east-1' ? 'block' : 'none');


  document.getElementById('tab-us-west-1').style.display       = 
    (region == 'us-west-1' ? 'block' : 'none');


  document.getElementById('tab-us-west-2').style.display       = 
    (region == 'us-west-2' ? 'block' : 'none');


  document.getElementById('tab-eu-central-1').style.display       = 
    (region == 'eu-central-1' ? 'block' : 'none');


  document.getElementById('tab-eu-west-1').style.display       = 
    (region == 'eu-west-1' ? 'block' : 'none');


  document.getElementById('tab-ap-northeast-1').style.display       = 
    (region == 'ap-northeast-1' ? 'block' : 'none');


  document.getElementById('tab-ap-southeast-1').style.display       = 
    (region == 'ap-southeast-1' ? 'block' : 'none');


  document.getElementById('tab-ap-southeast-2').style.display       = 
    (region == 'ap-southeast-2' ? 'block' : 'none');


  document.getElementById('tab-sa-east-1').style.display       = 
    (region == 'sa-east-1' ? 'block' : 'none');


  document.getElementById('tab-cn-north-1').style.display       = 
    (region == 'cn-north-1' ? 'block' : 'none');


  document.getElementById('tab-us-gov-west-1').style.display       = 
    (region == 'us-gov-west-1' ? 'block' : 'none');


}

//]]></script>

<div class="widget">
  <h3 class="widget-header">Ubuntu AMIs</h3>
    <div class="widget-content">

<!-- ###################################################################### -->

<form>
Ubuntu AMIs for EC2: 
<select name="selectregion" onchange='ON(this.form.selectregion.value);'>
<option value="">Select EC2 Region</option>
  <option value="us-east-1">us-east-1</option>
  <option value="us-west-1">us-west-1</option>
  <option value="us-west-2">us-west-2</option>
  <option value="eu-central-1">eu-central-1</option>
  <option value="eu-west-1">eu-west-1</option>
  <option value="ap-northeast-1">ap-northeast-1</option>
  <option value="ap-southeast-1">ap-southeast-1</option>
  <option value="ap-southeast-2">ap-southeast-2</option>
  <option value="sa-east-1">sa-east-1</option>
  <option value="cn-north-1">cn-north-1</option>
  <option value="us-gov-west-1">us-gov-west-1</option>
</select>
</form>

<!-- ###################################################################### -->
<div id="tab-us-east-1" style="display:none;">
            <table class="amis">
              <tbody>


              <tr>
                <th class="first">Ubuntu Release</th>
                <th>server<br>64-bit</th>
              </tr>

              <tr>
                <td class="first">Ubuntu 15.04 Vivid<br />
                PV EBS-SSD boot</td>
<td><tt>ami-bccccdd4&nbsp;<a title="Launch EC2 Instance on AWS Console" href="https://console.aws.amazon.com/ec2/home?region=us-east-1#launchAmi=ami-bccccdd4" target="_blank"><img src="/img/aws-launch-13x15.png" width="13" height="15" style="vertical-align:text-bottom"></a></tt></td>
              </tr>
              <tr>
                <td class="first">Ubuntu 15.04 Vivid<br />
                HVM EBS-SSD boot</td>
<td><tt>ami-b4cccddc&nbsp;<a title="Launch EC2 Instance on AWS Console" href="https://console.aws.amazon.com/ec2/home?region=us-east-1#launchAmi=ami-b4cccddc" target="_blank"><img src="/img/aws-launch-13x15.png" width="13" height="15" style="vertical-align:text-bottom"></a></tt></td>
              </tr>

              <tr>
                <th colspan="5"></th>
              </tr>

              <tr>
                <td class="first">Ubuntu 14.10 Utopic<br />
                PV EBS-SSD boot</td>
<td><tt>ami-10793a78&nbsp;<a title="Launch EC2 Instance on AWS Console" href="https://console.aws.amazon.com/ec2/home?region=us-east-1#launchAmi=ami-10793a78" target="_blank"><img src="/img/aws-launch-13x15.png" width="13" height="15" style="vertical-align:text-bottom"></a></tt></td>
              </tr>
              <tr>
                <td class="first">Ubuntu 14.10 Utopic<br />
                HVM EBS-SSD boot</td>
<td><tt>ami-ee793a86&nbsp;<a title="Launch EC2 Instance on AWS Console" href="https://console.aws.amazon.com/ec2/home?region=us-east-1#launchAmi=ami-ee793a86" target="_blank"><img src="/img/aws-launch-13x15.png" width="13" height="15" style="vertical-align:text-bottom"></a></tt></td>
              </tr>

              <tr>
                <th colspan="5"></th>
              </tr>

              <tr>
                <td class="first">Ubuntu 14.04 LTS Trusty<br />
                PV EBS-SSD boot</td>
<td><tt>ami-f43b3e9c&nbsp;<a title="Launch EC2 Instance on AWS Console" href="https://console.aws.amazon.com/ec2/home?region=us-east-1#launchAmi=ami-f43b3e9c" target="_blank"><img src="/img/aws-launch-13x15.png" width="13" height="15" style="vertical-align:text-bottom"></a></tt></td>
              </tr>
              <tr>
                <td class="first">Ubuntu 14.04 LTS Trusty<br />
                HVM EBS-SSD boot</td>
<td><tt>ami-cc3b3ea4&nbsp;<a title="Launch EC2 Instance on AWS Console" href="https://console.aws.amazon.com/ec2/home?region=us-east-1#launchAmi=ami-cc3b3ea4" target="_blank"><img src="/img/aws-launch-13x15.png" width="13" height="15" style="vertical-align:text-bottom"></a></tt></td>
              </tr>

              <tr>
                <th colspan="5"></th>
              </tr>

              <tr>
                <td class="first">Ubuntu 12.04 LTS Precise<br />
                PV EBS-SSD boot</td>
<td><tt>ami-d8132bb0&nbsp;<a title="Launch EC2 Instance on AWS Console" href="https://console.aws.amazon.com/ec2/home?region=us-east-1#launchAmi=ami-d8132bb0" target="_blank"><img src="/img/aws-launch-13x15.png" width="13" height="15" style="vertical-align:text-bottom"></a></tt></td>
              </tr>
              <tr>
                <td class="first">Ubuntu 12.04 LTS Precise<br />
                HVM EBS-SSD boot</td>
<td><tt>ami-d4132bbc&nbsp;<a title="Launch EC2 Instance on AWS Console" href="https://console.aws.amazon.com/ec2/home?region=us-east-1#launchAmi=ami-d4132bbc" target="_blank"><img src="/img/aws-launch-13x15.png" width="13" height="15" style="vertical-align:text-bottom"></a></tt></td>
              </tr>

              <tr>
                <th colspan="5"></th>
              </tr>


            </tbody></table>
</div>
<!-- ###################################################################### -->
<div id="tab-us-west-1" style="display:none;">
            <table class="amis">
              <tbody>


              <tr>
                <th class="first">Ubuntu Release</th>
                <th>server<br>64-bit</th>
              </tr>

              <tr>
                <td class="first">Ubuntu 15.04 Vivid<br />
                PV EBS-SSD boot</td>
<td><tt>ami-7d2bc639&nbsp;<a title="Launch EC2 Instance on AWS Console" href="https://console.aws.amazon.com/ec2/home?region=us-west-1#launchAmi=ami-7d2bc639" target="_blank"><img src="/img/aws-launch-13x15.png" width="13" height="15" style="vertical-align:text-bottom"></a></tt></td>
              </tr>
              <tr>
                <td class="first">Ubuntu 15.04 Vivid<br />
                HVM EBS-SSD boot</td>
<td><tt>ami-052bc641&nbsp;<a title="Launch EC2 Instance on AWS Console" href="https://console.aws.amazon.com/ec2/home?region=us-west-1#launchAmi=ami-052bc641" target="_blank"><img src="/img/aws-launch-13x15.png" width="13" height="15" style="vertical-align:text-bottom"></a></tt></td>
              </tr>

              <tr>
                <th colspan="5"></th>
              </tr>

              <tr>
                <td class="first">Ubuntu 14.10 Utopic<br />
                PV EBS-SSD boot</td>
<td><tt>ami-6cbca429&nbsp;<a title="Launch EC2 Instance on AWS Console" href="https://console.aws.amazon.com/ec2/home?region=us-west-1#launchAmi=ami-6cbca429" target="_blank"><img src="/img/aws-launch-13x15.png" width="13" height="15" style="vertical-align:text-bottom"></a></tt></td>
              </tr>
              <tr>
                <td class="first">Ubuntu 14.10 Utopic<br />
                HVM EBS-SSD boot</td>
<td><tt>ami-6abca42f&nbsp;<a title="Launch EC2 Instance on AWS Console" href="https://console.aws.amazon.com/ec2/home?region=us-west-1#launchAmi=ami-6abca42f" target="_blank"><img src="/img/aws-launch-13x15.png" width="13" height="15" style="vertical-align:text-bottom"></a></tt></td>
              </tr>

              <tr>
                <th colspan="5"></th>
              </tr>

              <tr>
                <td class="first">Ubuntu 14.04 LTS Trusty<br />
                PV EBS-SSD boot</td>
<td><tt>ami-7b7f9d3f&nbsp;<a title="Launch EC2 Instance on AWS Console" href="https://console.aws.amazon.com/ec2/home?region=us-west-1#launchAmi=ami-7b7f9d3f" target="_blank"><img src="/img/aws-launch-13x15.png" width="13" height="15" style="vertical-align:text-bottom"></a></tt></td>
              </tr>
              <tr>
                <td class="first">Ubuntu 14.04 LTS Trusty<br />
                HVM EBS-SSD boot</td>
<td><tt>ami-017f9d45&nbsp;<a title="Launch EC2 Instance on AWS Console" href="https://console.aws.amazon.com/ec2/home?region=us-west-1#launchAmi=ami-017f9d45" target="_blank"><img src="/img/aws-launch-13x15.png" width="13" height="15" style="vertical-align:text-bottom"></a></tt></td>
              </tr>

              <tr>
                <th colspan="5"></th>
              </tr>

              <tr>
                <td class="first">Ubuntu 12.04 LTS Precise<br />
                PV EBS-SSD boot</td>
<td><tt>ami-dffb199b&nbsp;<a title="Launch EC2 Instance on AWS Console" href="https://console.aws.amazon.com/ec2/home?region=us-west-1#launchAmi=ami-dffb199b" target="_blank"><img src="/img/aws-launch-13x15.png" width="13" height="15" style="vertical-align:text-bottom"></a></tt></td>
              </tr>
              <tr>
                <td class="first">Ubuntu 12.04 LTS Precise<br />
                HVM EBS-SSD boot</td>
<td><tt>ami-e1fb19a5&nbsp;<a title="Launch EC2 Instance on AWS Console" href="https://console.aws.amazon.com/ec2/home?region=us-west-1#launchAmi=ami-e1fb19a5" target="_blank"><img src="/img/aws-launch-13x15.png" width="13" height="15" style="vertical-align:text-bottom"></a></tt></td>
              </tr>

              <tr>
                <th colspan="5"></th>
              </tr>


            </tbody></table>
</div>
<!-- ###################################################################### -->
<div id="tab-us-west-2" style="display:none;">
            <table class="amis">
              <tbody>


              <tr>
                <th class="first">Ubuntu Release</th>
                <th>server<br>64-bit</th>
              </tr>

              <tr>
                <td class="first">Ubuntu 15.04 Vivid<br />
                PV EBS-SSD boot</td>
<td><tt>ami-27102417&nbsp;<a title="Launch EC2 Instance on AWS Console" href="https://console.aws.amazon.com/ec2/home?region=us-west-2#launchAmi=ami-27102417" target="_blank"><img src="/img/aws-launch-13x15.png" width="13" height="15" style="vertical-align:text-bottom"></a></tt></td>
              </tr>
              <tr>
                <td class="first">Ubuntu 15.04 Vivid<br />
                HVM EBS-SSD boot</td>
<td><tt>ami-2d10241d&nbsp;<a title="Launch EC2 Instance on AWS Console" href="https://console.aws.amazon.com/ec2/home?region=us-west-2#launchAmi=ami-2d10241d" target="_blank"><img src="/img/aws-launch-13x15.png" width="13" height="15" style="vertical-align:text-bottom"></a></tt></td>
              </tr>

              <tr>
                <th colspan="5"></th>
              </tr>

              <tr>
                <td class="first">Ubuntu 14.10 Utopic<br />
                PV EBS-SSD boot</td>
<td><tt>ami-b5471c85&nbsp;<a title="Launch EC2 Instance on AWS Console" href="https://console.aws.amazon.com/ec2/home?region=us-west-2#launchAmi=ami-b5471c85" target="_blank"><img src="/img/aws-launch-13x15.png" width="13" height="15" style="vertical-align:text-bottom"></a></tt></td>
              </tr>
              <tr>
                <td class="first">Ubuntu 14.10 Utopic<br />
                HVM EBS-SSD boot</td>
<td><tt>ami-bd471c8d&nbsp;<a title="Launch EC2 Instance on AWS Console" href="https://console.aws.amazon.com/ec2/home?region=us-west-2#launchAmi=ami-bd471c8d" target="_blank"><img src="/img/aws-launch-13x15.png" width="13" height="15" style="vertical-align:text-bottom"></a></tt></td>
              </tr>

              <tr>
                <th colspan="5"></th>
              </tr>

              <tr>
                <td class="first">Ubuntu 14.04 LTS Trusty<br />
                PV EBS-SSD boot</td>
<td><tt>ami-6f52675f&nbsp;<a title="Launch EC2 Instance on AWS Console" href="https://console.aws.amazon.com/ec2/home?region=us-west-2#launchAmi=ami-6f52675f" target="_blank"><img src="/img/aws-launch-13x15.png" width="13" height="15" style="vertical-align:text-bottom"></a></tt></td>
              </tr>
              <tr>
                <td class="first">Ubuntu 14.04 LTS Trusty<br />
                HVM EBS-SSD boot</td>
<td><tt>ami-55526765&nbsp;<a title="Launch EC2 Instance on AWS Console" href="https://console.aws.amazon.com/ec2/home?region=us-west-2#launchAmi=ami-55526765" target="_blank"><img src="/img/aws-launch-13x15.png" width="13" height="15" style="vertical-align:text-bottom"></a></tt></td>
              </tr>

              <tr>
                <th colspan="5"></th>
              </tr>

              <tr>
                <td class="first">Ubuntu 12.04 LTS Precise<br />
                PV EBS-SSD boot</td>
<td><tt>ami-ed557fdd&nbsp;<a title="Launch EC2 Instance on AWS Console" href="https://console.aws.amazon.com/ec2/home?region=us-west-2#launchAmi=ami-ed557fdd" target="_blank"><img src="/img/aws-launch-13x15.png" width="13" height="15" style="vertical-align:text-bottom"></a></tt></td>
              </tr>
              <tr>
                <td class="first">Ubuntu 12.04 LTS Precise<br />
                HVM EBS-SSD boot</td>
<td><tt>ami-d9557fe9&nbsp;<a title="Launch EC2 Instance on AWS Console" href="https://console.aws.amazon.com/ec2/home?region=us-west-2#launchAmi=ami-d9557fe9" target="_blank"><img src="/img/aws-launch-13x15.png" width="13" height="15" style="vertical-align:text-bottom"></a></tt></td>
              </tr>

              <tr>
                <th colspan="5"></th>
              </tr>


            </tbody></table>
</div>
<!-- ###################################################################### -->
<div id="tab-eu-central-1" style="display:none;">
            <table class="amis">
              <tbody>


              <tr>
                <th class="first">Ubuntu Release</th>
                <th>server<br>64-bit</th>
              </tr>

              <tr>
                <td class="first">Ubuntu 15.04 Vivid<br />
                PV EBS-SSD boot</td>
<td><tt>ami-5e9da143&nbsp;<a title="Launch EC2 Instance on AWS Console" href="https://console.aws.amazon.com/ec2/home?region=eu-central-1#launchAmi=ami-5e9da143" target="_blank"><img src="/img/aws-launch-13x15.png" width="13" height="15" style="vertical-align:text-bottom"></a></tt></td>
              </tr>
              <tr>
                <td class="first">Ubuntu 15.04 Vivid<br />
                HVM EBS-SSD boot</td>
<td><tt>ami-549da149&nbsp;<a title="Launch EC2 Instance on AWS Console" href="https://console.aws.amazon.com/ec2/home?region=eu-central-1#launchAmi=ami-549da149" target="_blank"><img src="/img/aws-launch-13x15.png" width="13" height="15" style="vertical-align:text-bottom"></a></tt></td>
              </tr>

              <tr>
                <th colspan="5"></th>
              </tr>

              <tr>
                <td class="first">Ubuntu 14.10 Utopic<br />
                PV EBS-SSD boot</td>
<td><tt>ami-54c2f149&nbsp;<a title="Launch EC2 Instance on AWS Console" href="https://console.aws.amazon.com/ec2/home?region=eu-central-1#launchAmi=ami-54c2f149" target="_blank"><img src="/img/aws-launch-13x15.png" width="13" height="15" style="vertical-align:text-bottom"></a></tt></td>
              </tr>
              <tr>
                <td class="first">Ubuntu 14.10 Utopic<br />
                HVM EBS-SSD boot</td>
<td><tt>ami-52c2f14f&nbsp;<a title="Launch EC2 Instance on AWS Console" href="https://console.aws.amazon.com/ec2/home?region=eu-central-1#launchAmi=ami-52c2f14f" target="_blank"><img src="/img/aws-launch-13x15.png" width="13" height="15" style="vertical-align:text-bottom"></a></tt></td>
              </tr>

              <tr>
                <th colspan="5"></th>
              </tr>

              <tr>
                <td class="first">Ubuntu 14.04 LTS Trusty<br />
                PV EBS-SSD boot</td>
<td><tt>ami-06dae61b&nbsp;<a title="Launch EC2 Instance on AWS Console" href="https://console.aws.amazon.com/ec2/home?region=eu-central-1#launchAmi=ami-06dae61b" target="_blank"><img src="/img/aws-launch-13x15.png" width="13" height="15" style="vertical-align:text-bottom"></a></tt></td>
              </tr>
              <tr>
                <td class="first">Ubuntu 14.04 LTS Trusty<br />
                HVM EBS-SSD boot</td>
<td><tt>ami-3cdae621&nbsp;<a title="Launch EC2 Instance on AWS Console" href="https://console.aws.amazon.com/ec2/home?region=eu-central-1#launchAmi=ami-3cdae621" target="_blank"><img src="/img/aws-launch-13x15.png" width="13" height="15" style="vertical-align:text-bottom"></a></tt></td>
              </tr>

              <tr>
                <th colspan="5"></th>
              </tr>

              <tr>
                <td class="first">Ubuntu 12.04 LTS Precise<br />
                PV EBS-SSD boot</td>
<td><tt>ami-00003c1d&nbsp;<a title="Launch EC2 Instance on AWS Console" href="https://console.aws.amazon.com/ec2/home?region=eu-central-1#launchAmi=ami-00003c1d" target="_blank"><img src="/img/aws-launch-13x15.png" width="13" height="15" style="vertical-align:text-bottom"></a></tt></td>
              </tr>
              <tr>
                <td class="first">Ubuntu 12.04 LTS Precise<br />
                HVM EBS-SSD boot</td>
<td><tt>ami-3e003c23&nbsp;<a title="Launch EC2 Instance on AWS Console" href="https://console.aws.amazon.com/ec2/home?region=eu-central-1#launchAmi=ami-3e003c23" target="_blank"><img src="/img/aws-launch-13x15.png" width="13" height="15" style="vertical-align:text-bottom"></a></tt></td>
              </tr>

              <tr>
                <th colspan="5"></th>
              </tr>


            </tbody></table>
</div>
<!-- ###################################################################### -->
<div id="tab-eu-west-1" style="display:none;">
            <table class="amis">
              <tbody>


              <tr>
                <th class="first">Ubuntu Release</th>
                <th>server<br>64-bit</th>
              </tr>

              <tr>
                <td class="first">Ubuntu 15.04 Vivid<br />
                PV EBS-SSD boot</td>
<td><tt>ami-c987e5be&nbsp;<a title="Launch EC2 Instance on AWS Console" href="https://console.aws.amazon.com/ec2/home?region=eu-west-1#launchAmi=ami-c987e5be" target="_blank"><img src="/img/aws-launch-13x15.png" width="13" height="15" style="vertical-align:text-bottom"></a></tt></td>
              </tr>
              <tr>
                <td class="first">Ubuntu 15.04 Vivid<br />
                HVM EBS-SSD boot</td>
<td><tt>ami-b387e5c4&nbsp;<a title="Launch EC2 Instance on AWS Console" href="https://console.aws.amazon.com/ec2/home?region=eu-west-1#launchAmi=ami-b387e5c4" target="_blank"><img src="/img/aws-launch-13x15.png" width="13" height="15" style="vertical-align:text-bottom"></a></tt></td>
              </tr>

              <tr>
                <th colspan="5"></th>
              </tr>

              <tr>
                <td class="first">Ubuntu 14.10 Utopic<br />
                PV EBS-SSD boot</td>
<td><tt>ami-519e1026&nbsp;<a title="Launch EC2 Instance on AWS Console" href="https://console.aws.amazon.com/ec2/home?region=eu-west-1#launchAmi=ami-519e1026" target="_blank"><img src="/img/aws-launch-13x15.png" width="13" height="15" style="vertical-align:text-bottom"></a></tt></td>
              </tr>
              <tr>
                <td class="first">Ubuntu 14.10 Utopic<br />
                HVM EBS-SSD boot</td>
<td><tt>ami-5b9e102c&nbsp;<a title="Launch EC2 Instance on AWS Console" href="https://console.aws.amazon.com/ec2/home?region=eu-west-1#launchAmi=ami-5b9e102c" target="_blank"><img src="/img/aws-launch-13x15.png" width="13" height="15" style="vertical-align:text-bottom"></a></tt></td>
              </tr>

              <tr>
                <th colspan="5"></th>
              </tr>

              <tr>
                <td class="first">Ubuntu 14.04 LTS Trusty<br />
                PV EBS-SSD boot</td>
<td><tt>ami-2596f652&nbsp;<a title="Launch EC2 Instance on AWS Console" href="https://console.aws.amazon.com/ec2/home?region=eu-west-1#launchAmi=ami-2596f652" target="_blank"><img src="/img/aws-launch-13x15.png" width="13" height="15" style="vertical-align:text-bottom"></a></tt></td>
              </tr>
              <tr>
                <td class="first">Ubuntu 14.04 LTS Trusty<br />
                HVM EBS-SSD boot</td>
<td><tt>ami-2d96f65a&nbsp;<a title="Launch EC2 Instance on AWS Console" href="https://console.aws.amazon.com/ec2/home?region=eu-west-1#launchAmi=ami-2d96f65a" target="_blank"><img src="/img/aws-launch-13x15.png" width="13" height="15" style="vertical-align:text-bottom"></a></tt></td>
              </tr>

              <tr>
                <th colspan="5"></th>
              </tr>

              <tr>
                <td class="first">Ubuntu 12.04 LTS Precise<br />
                PV EBS-SSD boot</td>
<td><tt>ami-d97e1fae&nbsp;<a title="Launch EC2 Instance on AWS Console" href="https://console.aws.amazon.com/ec2/home?region=eu-west-1#launchAmi=ami-d97e1fae" target="_blank"><img src="/img/aws-launch-13x15.png" width="13" height="15" style="vertical-align:text-bottom"></a></tt></td>
              </tr>
              <tr>
                <td class="first">Ubuntu 12.04 LTS Precise<br />
                HVM EBS-SSD boot</td>
<td><tt>ami-cd7e1fba&nbsp;<a title="Launch EC2 Instance on AWS Console" href="https://console.aws.amazon.com/ec2/home?region=eu-west-1#launchAmi=ami-cd7e1fba" target="_blank"><img src="/img/aws-launch-13x15.png" width="13" height="15" style="vertical-align:text-bottom"></a></tt></td>
              </tr>

              <tr>
                <th colspan="5"></th>
              </tr>


            </tbody></table>
</div>
<!-- ###################################################################### -->
<div id="tab-ap-northeast-1" style="display:none;">
            <table class="amis">
              <tbody>


              <tr>
                <th class="first">Ubuntu Release</th>
                <th>server<br>64-bit</th>
              </tr>

              <tr>
                <td class="first">Ubuntu 15.04 Vivid<br />
                PV EBS-SSD boot</td>
<td><tt>ami-5ca1675c&nbsp;<a title="Launch EC2 Instance on AWS Console" href="https://console.aws.amazon.com/ec2/home?region=ap-northeast-1#launchAmi=ami-5ca1675c" target="_blank"><img src="/img/aws-launch-13x15.png" width="13" height="15" style="vertical-align:text-bottom"></a></tt></td>
              </tr>
              <tr>
                <td class="first">Ubuntu 15.04 Vivid<br />
                HVM EBS-SSD boot</td>
<td><tt>ami-64a16764&nbsp;<a title="Launch EC2 Instance on AWS Console" href="https://console.aws.amazon.com/ec2/home?region=ap-northeast-1#launchAmi=ami-64a16764" target="_blank"><img src="/img/aws-launch-13x15.png" width="13" height="15" style="vertical-align:text-bottom"></a></tt></td>
              </tr>

              <tr>
                <th colspan="5"></th>
              </tr>

              <tr>
                <td class="first">Ubuntu 14.10 Utopic<br />
                PV EBS-SSD boot</td>
<td><tt>ami-5cbca75d&nbsp;<a title="Launch EC2 Instance on AWS Console" href="https://console.aws.amazon.com/ec2/home?region=ap-northeast-1#launchAmi=ami-5cbca75d" target="_blank"><img src="/img/aws-launch-13x15.png" width="13" height="15" style="vertical-align:text-bottom"></a></tt></td>
              </tr>
              <tr>
                <td class="first">Ubuntu 14.10 Utopic<br />
                HVM EBS-SSD boot</td>
<td><tt>ami-80bca781&nbsp;<a title="Launch EC2 Instance on AWS Console" href="https://console.aws.amazon.com/ec2/home?region=ap-northeast-1#launchAmi=ami-80bca781" target="_blank"><img src="/img/aws-launch-13x15.png" width="13" height="15" style="vertical-align:text-bottom"></a></tt></td>
              </tr>

              <tr>
                <th colspan="5"></th>
              </tr>

              <tr>
                <td class="first">Ubuntu 14.04 LTS Trusty<br />
                PV EBS-SSD boot</td>
<td><tt>ami-ba11d4ba&nbsp;<a title="Launch EC2 Instance on AWS Console" href="https://console.aws.amazon.com/ec2/home?region=ap-northeast-1#launchAmi=ami-ba11d4ba" target="_blank"><img src="/img/aws-launch-13x15.png" width="13" height="15" style="vertical-align:text-bottom"></a></tt></td>
              </tr>
              <tr>
                <td class="first">Ubuntu 14.04 LTS Trusty<br />
                HVM EBS-SSD boot</td>
<td><tt>ami-fc11d4fc&nbsp;<a title="Launch EC2 Instance on AWS Console" href="https://console.aws.amazon.com/ec2/home?region=ap-northeast-1#launchAmi=ami-fc11d4fc" target="_blank"><img src="/img/aws-launch-13x15.png" width="13" height="15" style="vertical-align:text-bottom"></a></tt></td>
              </tr>

              <tr>
                <th colspan="5"></th>
              </tr>

              <tr>
                <td class="first">Ubuntu 12.04 LTS Precise<br />
                PV EBS-SSD boot</td>
<td><tt>ami-18ba4018&nbsp;<a title="Launch EC2 Instance on AWS Console" href="https://console.aws.amazon.com/ec2/home?region=ap-northeast-1#launchAmi=ami-18ba4018" target="_blank"><img src="/img/aws-launch-13x15.png" width="13" height="15" style="vertical-align:text-bottom"></a></tt></td>
              </tr>
              <tr>
                <td class="first">Ubuntu 12.04 LTS Precise<br />
                HVM EBS-SSD boot</td>
<td><tt>ami-1eba401e&nbsp;<a title="Launch EC2 Instance on AWS Console" href="https://console.aws.amazon.com/ec2/home?region=ap-northeast-1#launchAmi=ami-1eba401e" target="_blank"><img src="/img/aws-launch-13x15.png" width="13" height="15" style="vertical-align:text-bottom"></a></tt></td>
              </tr>

              <tr>
                <th colspan="5"></th>
              </tr>


            </tbody></table>
</div>
<!-- ###################################################################### -->
<div id="tab-ap-southeast-1" style="display:none;">
            <table class="amis">
              <tbody>


              <tr>
                <th class="first">Ubuntu Release</th>
                <th>server<br>64-bit</th>
              </tr>

              <tr>
                <td class="first">Ubuntu 15.04 Vivid<br />
                PV EBS-SSD boot</td>
<td><tt>ami-50b08d02&nbsp;<a title="Launch EC2 Instance on AWS Console" href="https://console.aws.amazon.com/ec2/home?region=ap-southeast-1#launchAmi=ami-50b08d02" target="_blank"><img src="/img/aws-launch-13x15.png" width="13" height="15" style="vertical-align:text-bottom"></a></tt></td>
              </tr>
              <tr>
                <td class="first">Ubuntu 15.04 Vivid<br />
                HVM EBS-SSD boot</td>
<td><tt>ami-5eb08d0c&nbsp;<a title="Launch EC2 Instance on AWS Console" href="https://console.aws.amazon.com/ec2/home?region=ap-southeast-1#launchAmi=ami-5eb08d0c" target="_blank"><img src="/img/aws-launch-13x15.png" width="13" height="15" style="vertical-align:text-bottom"></a></tt></td>
              </tr>

              <tr>
                <th colspan="5"></th>
              </tr>

              <tr>
                <td class="first">Ubuntu 14.10 Utopic<br />
                PV EBS-SSD boot</td>
<td><tt>ami-16c6ec44&nbsp;<a title="Launch EC2 Instance on AWS Console" href="https://console.aws.amazon.com/ec2/home?region=ap-southeast-1#launchAmi=ami-16c6ec44" target="_blank"><img src="/img/aws-launch-13x15.png" width="13" height="15" style="vertical-align:text-bottom"></a></tt></td>
              </tr>
              <tr>
                <td class="first">Ubuntu 14.10 Utopic<br />
                HVM EBS-SSD boot</td>
<td><tt>ami-34c6ec66&nbsp;<a title="Launch EC2 Instance on AWS Console" href="https://console.aws.amazon.com/ec2/home?region=ap-southeast-1#launchAmi=ami-34c6ec66" target="_blank"><img src="/img/aws-launch-13x15.png" width="13" height="15" style="vertical-align:text-bottom"></a></tt></td>
              </tr>

              <tr>
                <th colspan="5"></th>
              </tr>

              <tr>
                <td class="first">Ubuntu 14.04 LTS Trusty<br />
                PV EBS-SSD boot</td>
<td><tt>ami-4c54691e&nbsp;<a title="Launch EC2 Instance on AWS Console" href="https://console.aws.amazon.com/ec2/home?region=ap-southeast-1#launchAmi=ami-4c54691e" target="_blank"><img src="/img/aws-launch-13x15.png" width="13" height="15" style="vertical-align:text-bottom"></a></tt></td>
              </tr>
              <tr>
                <td class="first">Ubuntu 14.04 LTS Trusty<br />
                HVM EBS-SSD boot</td>
<td><tt>ami-7854692a&nbsp;<a title="Launch EC2 Instance on AWS Console" href="https://console.aws.amazon.com/ec2/home?region=ap-southeast-1#launchAmi=ami-7854692a" target="_blank"><img src="/img/aws-launch-13x15.png" width="13" height="15" style="vertical-align:text-bottom"></a></tt></td>
              </tr>

              <tr>
                <th colspan="5"></th>
              </tr>

              <tr>
                <td class="first">Ubuntu 12.04 LTS Precise<br />
                PV EBS-SSD boot</td>
<td><tt>ami-5acefc08&nbsp;<a title="Launch EC2 Instance on AWS Console" href="https://console.aws.amazon.com/ec2/home?region=ap-southeast-1#launchAmi=ami-5acefc08" target="_blank"><img src="/img/aws-launch-13x15.png" width="13" height="15" style="vertical-align:text-bottom"></a></tt></td>
              </tr>
              <tr>
                <td class="first">Ubuntu 12.04 LTS Precise<br />
                HVM EBS-SSD boot</td>
<td><tt>ami-5ccefc0e&nbsp;<a title="Launch EC2 Instance on AWS Console" href="https://console.aws.amazon.com/ec2/home?region=ap-southeast-1#launchAmi=ami-5ccefc0e" target="_blank"><img src="/img/aws-launch-13x15.png" width="13" height="15" style="vertical-align:text-bottom"></a></tt></td>
              </tr>

              <tr>
                <th colspan="5"></th>
              </tr>


            </tbody></table>
</div>
<!-- ###################################################################### -->
<div id="tab-ap-southeast-2" style="display:none;">
            <table class="amis">
              <tbody>


              <tr>
                <th class="first">Ubuntu Release</th>
                <th>server<br>64-bit</th>
              </tr>

              <tr>
                <td class="first">Ubuntu 15.04 Vivid<br />
                PV EBS-SSD boot</td>
<td><tt>ami-0bec9131&nbsp;<a title="Launch EC2 Instance on AWS Console" href="https://console.aws.amazon.com/ec2/home?region=ap-southeast-2#launchAmi=ami-0bec9131" target="_blank"><img src="/img/aws-launch-13x15.png" width="13" height="15" style="vertical-align:text-bottom"></a></tt></td>
              </tr>
              <tr>
                <td class="first">Ubuntu 15.04 Vivid<br />
                HVM EBS-SSD boot</td>
<td><tt>ami-0dec9137&nbsp;<a title="Launch EC2 Instance on AWS Console" href="https://console.aws.amazon.com/ec2/home?region=ap-southeast-2#launchAmi=ami-0dec9137" target="_blank"><img src="/img/aws-launch-13x15.png" width="13" height="15" style="vertical-align:text-bottom"></a></tt></td>
              </tr>

              <tr>
                <th colspan="5"></th>
              </tr>

              <tr>
                <td class="first">Ubuntu 14.10 Utopic<br />
                PV EBS-SSD boot</td>
<td><tt>ami-d5eb9fef&nbsp;<a title="Launch EC2 Instance on AWS Console" href="https://console.aws.amazon.com/ec2/home?region=ap-southeast-2#launchAmi=ami-d5eb9fef" target="_blank"><img src="/img/aws-launch-13x15.png" width="13" height="15" style="vertical-align:text-bottom"></a></tt></td>
              </tr>
              <tr>
                <td class="first">Ubuntu 14.10 Utopic<br />
                HVM EBS-SSD boot</td>
<td><tt>ami-cdeb9ff7&nbsp;<a title="Launch EC2 Instance on AWS Console" href="https://console.aws.amazon.com/ec2/home?region=ap-southeast-2#launchAmi=ami-cdeb9ff7" target="_blank"><img src="/img/aws-launch-13x15.png" width="13" height="15" style="vertical-align:text-bottom"></a></tt></td>
              </tr>

              <tr>
                <th colspan="5"></th>
              </tr>

              <tr>
                <td class="first">Ubuntu 14.04 LTS Trusty<br />
                PV EBS-SSD boot</td>
<td><tt>ami-c9611cf3&nbsp;<a title="Launch EC2 Instance on AWS Console" href="https://console.aws.amazon.com/ec2/home?region=ap-southeast-2#launchAmi=ami-c9611cf3" target="_blank"><img src="/img/aws-launch-13x15.png" width="13" height="15" style="vertical-align:text-bottom"></a></tt></td>
              </tr>
              <tr>
                <td class="first">Ubuntu 14.04 LTS Trusty<br />
                HVM EBS-SSD boot</td>
<td><tt>ami-c5611cff&nbsp;<a title="Launch EC2 Instance on AWS Console" href="https://console.aws.amazon.com/ec2/home?region=ap-southeast-2#launchAmi=ami-c5611cff" target="_blank"><img src="/img/aws-launch-13x15.png" width="13" height="15" style="vertical-align:text-bottom"></a></tt></td>
              </tr>

              <tr>
                <th colspan="5"></th>
              </tr>

              <tr>
                <td class="first">Ubuntu 12.04 LTS Precise<br />
                PV EBS-SSD boot</td>
<td><tt>ami-933944a9&nbsp;<a title="Launch EC2 Instance on AWS Console" href="https://console.aws.amazon.com/ec2/home?region=ap-southeast-2#launchAmi=ami-933944a9" target="_blank"><img src="/img/aws-launch-13x15.png" width="13" height="15" style="vertical-align:text-bottom"></a></tt></td>
              </tr>
              <tr>
                <td class="first">Ubuntu 12.04 LTS Precise<br />
                HVM EBS-SSD boot</td>
<td><tt>ami-953944af&nbsp;<a title="Launch EC2 Instance on AWS Console" href="https://console.aws.amazon.com/ec2/home?region=ap-southeast-2#launchAmi=ami-953944af" target="_blank"><img src="/img/aws-launch-13x15.png" width="13" height="15" style="vertical-align:text-bottom"></a></tt></td>
              </tr>

              <tr>
                <th colspan="5"></th>
              </tr>


            </tbody></table>
</div>
<!-- ###################################################################### -->
<div id="tab-sa-east-1" style="display:none;">
            <table class="amis">
              <tbody>


              <tr>
                <th class="first">Ubuntu Release</th>
                <th>server<br>64-bit</th>
              </tr>

              <tr>
                <td class="first">Ubuntu 15.04 Vivid<br />
                PV EBS-SSD boot</td>
<td><tt>ami-6931b474&nbsp;<a title="Launch EC2 Instance on AWS Console" href="https://console.aws.amazon.com/ec2/home?region=sa-east-1#launchAmi=ami-6931b474" target="_blank"><img src="/img/aws-launch-13x15.png" width="13" height="15" style="vertical-align:text-bottom"></a></tt></td>
              </tr>
              <tr>
                <td class="first">Ubuntu 15.04 Vivid<br />
                HVM EBS-SSD boot</td>
<td><tt>ami-6731b47a&nbsp;<a title="Launch EC2 Instance on AWS Console" href="https://console.aws.amazon.com/ec2/home?region=sa-east-1#launchAmi=ami-6731b47a" target="_blank"><img src="/img/aws-launch-13x15.png" width="13" height="15" style="vertical-align:text-bottom"></a></tt></td>
              </tr>

              <tr>
                <th colspan="5"></th>
              </tr>

              <tr>
                <td class="first">Ubuntu 14.10 Utopic<br />
                PV EBS-SSD boot</td>
<td><tt>ami-87f14e9a&nbsp;<a title="Launch EC2 Instance on AWS Console" href="https://console.aws.amazon.com/ec2/home?region=sa-east-1#launchAmi=ami-87f14e9a" target="_blank"><img src="/img/aws-launch-13x15.png" width="13" height="15" style="vertical-align:text-bottom"></a></tt></td>
              </tr>
              <tr>
                <td class="first">Ubuntu 14.10 Utopic<br />
                HVM EBS-SSD boot</td>
<td><tt>ami-bdf14ea0&nbsp;<a title="Launch EC2 Instance on AWS Console" href="https://console.aws.amazon.com/ec2/home?region=sa-east-1#launchAmi=ami-bdf14ea0" target="_blank"><img src="/img/aws-launch-13x15.png" width="13" height="15" style="vertical-align:text-bottom"></a></tt></td>
              </tr>

              <tr>
                <th colspan="5"></th>
              </tr>

              <tr>
                <td class="first">Ubuntu 14.04 LTS Trusty<br />
                PV EBS-SSD boot</td>
<td><tt>ami-79b23764&nbsp;<a title="Launch EC2 Instance on AWS Console" href="https://console.aws.amazon.com/ec2/home?region=sa-east-1#launchAmi=ami-79b23764" target="_blank"><img src="/img/aws-launch-13x15.png" width="13" height="15" style="vertical-align:text-bottom"></a></tt></td>
              </tr>
              <tr>
                <td class="first">Ubuntu 14.04 LTS Trusty<br />
                HVM EBS-SSD boot</td>
<td><tt>ami-71b2376c&nbsp;<a title="Launch EC2 Instance on AWS Console" href="https://console.aws.amazon.com/ec2/home?region=sa-east-1#launchAmi=ami-71b2376c" target="_blank"><img src="/img/aws-launch-13x15.png" width="13" height="15" style="vertical-align:text-bottom"></a></tt></td>
              </tr>

              <tr>
                <th colspan="5"></th>
              </tr>

              <tr>
                <td class="first">Ubuntu 12.04 LTS Precise<br />
                PV EBS-SSD boot</td>
<td><tt>ami-6be46176&nbsp;<a title="Launch EC2 Instance on AWS Console" href="https://console.aws.amazon.com/ec2/home?region=sa-east-1#launchAmi=ami-6be46176" target="_blank"><img src="/img/aws-launch-13x15.png" width="13" height="15" style="vertical-align:text-bottom"></a></tt></td>
              </tr>
              <tr>
                <td class="first">Ubuntu 12.04 LTS Precise<br />
                HVM EBS-SSD boot</td>
<td><tt>ami-63e4617e&nbsp;<a title="Launch EC2 Instance on AWS Console" href="https://console.aws.amazon.com/ec2/home?region=sa-east-1#launchAmi=ami-63e4617e" target="_blank"><img src="/img/aws-launch-13x15.png" width="13" height="15" style="vertical-align:text-bottom"></a></tt></td>
              </tr>

              <tr>
                <th colspan="5"></th>
              </tr>


            </tbody></table>
</div>
<!-- ###################################################################### -->
<div id="tab-cn-north-1" style="display:none;">
            <table class="amis">
              <tbody>


              <tr>
                <th class="first">Ubuntu Release</th>
                <th>server<br>64-bit</th>
              </tr>


              <tr>
                <th colspan="5"></th>
              </tr>


              <tr>
                <th colspan="5"></th>
              </tr>


              <tr>
                <th colspan="5"></th>
              </tr>


              <tr>
                <th colspan="5"></th>
              </tr>


            </tbody></table>
</div>
<!-- ###################################################################### -->
<div id="tab-us-gov-west-1" style="display:none;">
            <table class="amis">
              <tbody>


              <tr>
                <th class="first">Ubuntu Release</th>
                <th>server<br>64-bit</th>
              </tr>


              <tr>
                <th colspan="5"></th>
              </tr>


              <tr>
                <th colspan="5"></th>
              </tr>


              <tr>
                <th colspan="5"></th>
              </tr>


              <tr>
                <th colspan="5"></th>
              </tr>


            </tbody></table>
</div>

<p><br /></p>

<div id="ami-comments" style="display:none;">

<p>
The Ubuntu AMIs listed above are published by Canonical.
</p>

<p>
<a href="http://cloud-images.ubuntu.com/locator/ec2/">Ubuntu AMI finder</a> for many other types of AMIs including 32-bit, instance-store, EBS-magnetic, EBS-SSD pIOPS.
</p>
 
<a href="http://wiki.debian.org/Cloud/AmazonEC2Image">Official Debian AMIs</a> are also available.

</div>


    </div>
</div>
<div class="widget-recent-entries widget-archives widget">
    <h3 class="widget-header">More Entries</h3>
    <div class="widget-content">
        <dl>
        
            <dt><a href="http://alestic.com/2014/09/aws-root-password">Throw Away The Password To Your AWS Account</a></dt>
            <dd>reduce the risk of losing control of your AWS account by not knowing the root account password As Amazon states, one of the best practices for using AWS is Don&#8217;t&hellip;</dd>
<!-- 
            <dd class="entry-meta">By Eric Hammond | Comments (0)</dd>
-->
            <dd class="entry-meta"></dd>
        
    
        
            <dt><a href="http://alestic.com/2014/09/aws-community-heroes">AWS Community Heroes Program</a></dt>
            <dd>Amazon Web Services recently announced an AWS Community Heroes Program where they are starting to recognize publicly some of the many individuals around the world who contribute in so many&hellip;</dd>
<!-- 
            <dd class="entry-meta">By Eric Hammond | Comments (0)</dd>
-->
            <dd class="entry-meta"></dd>
        
    
        
            <dt><a href="http://alestic.com/2014/06/ec2-ebs-ssd-ami">EBS-SSD Boot AMIs For Ubuntu On Amazon EC2</a></dt>
            <dd>With Amazon&#8217;s announcement that SSD is now available for EBS volumes, they have also declared this the recommended EBS volume type. The good folks at Canonical are now building Ubuntu&hellip;</dd>
<!-- 
            <dd class="entry-meta">By Eric Hammond | Comments (2)</dd>
-->
            <dd class="entry-meta"></dd>
        
    
        
            <dt><a href="http://alestic.com/2014/02/ec2-create-image-reboot">EC2 create-image Does Not Fully "Stop" The Instance</a></dt>
            <dd>The EC2 create-image API/command/console action is a convenient trigger to create an AMI from a running (or stopped) EBS boot instance. It takes a snapshot of the instance&#8217;s EBS volume(s)&hellip;</dd>
<!-- 
            <dd class="entry-meta">By Eric Hammond | Comments (4)</dd>
-->
            <dd class="entry-meta"></dd>
        
    
        
            <dt><a href="http://alestic.com/2014/01/aws-region-search">Finding the Region for an AWS Resource ID</a></dt>
            <dd>use concurrent AWS command line requests to search the world for your instance, image, volume, snapshot, &#8230; Background Amazon EC2 and many other AWS services are divided up into various&hellip;</dd>
<!-- 
            <dd class="entry-meta">By Eric Hammond | Comments (2)</dd>
-->
            <dd class="entry-meta"></dd>
        
    
        
            <dt><a href="http://alestic.com/2014/01/ec2-change-username">Changing The Default "ubuntu" Username On New EC2 Instances</a></dt>
            <dd>configure your own ssh username in user-data The official Ubuntu AMIs create a default user with the username ubuntu which is used for the initial ssh access, i.e.: ssh ubuntu@&lt;HOST&gt;&hellip;</dd>
<!-- 
            <dd class="entry-meta">By Eric Hammond | Comments (4)</dd>
-->
            <dd class="entry-meta"></dd>
        
    
        
            <dt><a href="http://alestic.com/2014/01/ec2-ssh-username">Default ssh Usernames For Connecting To EC2 Instances</a></dt>
            <dd>Each AMI publisher on EC2 decides what user (or users) should have ssh access enabled by default and what ssh credentials should allow you to gain access as that user.&hellip;</dd>
<!-- 
            <dd class="entry-meta">By Eric Hammond | Comments (0)</dd>
-->
            <dd class="entry-meta"></dd>
        
    
        
            <dt><a href="http://alestic.com/2013/12/ec2-instance-type-c3">New c3.* Instance Types on Amazon EC2 - Nice!</a></dt>
            <dd>Worth switching. Amazon shared that the new c3.* instance types have been in high demand on EC2 since they were released. I finally had a minute to take a look&hellip;</dd>
<!-- 
            <dd class="entry-meta">By Eric Hammond | Comments (2)</dd>
-->
            <dd class="entry-meta"></dd>
        
    
        
            <dt><a href="http://alestic.com/2013/12/ec2-account-attributes">Query EC2 Account Limits with AWS API</a></dt>
            <dd>Here&#8217;s a useful tip mentioned in one of the sessions at AWS re:Invent this year. There is a little known API call that lets you query some of the EC2&hellip;</dd>
<!-- 
            <dd class="entry-meta">By Eric Hammond | Comments (4)</dd>
-->
            <dd class="entry-meta"></dd>
        
    
        
            <dt><a href="http://alestic.com/2013/11/aws-cli-query">Using aws-cli --query Option To Simplify Output</a></dt>
            <dd>My favorite session at AWS re:Invent was James Saryerwinnie&#8217;s clear, concise, and informative tour of the aws-cli (command line interface), which according to GitHub logs he is enhancing like crazy.&hellip;</dd>
<!-- 
            <dd class="entry-meta">By Eric Hammond | Comments (0)</dd>
-->
            <dd class="entry-meta"></dd>
        
    
        
            <dt><a href="http://alestic.com/2013/09/s3-lifecycle-extend">Reset S3 Object Timestamp for Bucket Lifecycle Expiration</a></dt>
            <dd>use aws-cli to extend expiration and restart the delete or archive countdown on objects in an S3 bucket Background S3 buckets allow you to specify lifecycle rules that tell AWS&hellip;</dd>
<!-- 
            <dd class="entry-meta">By Eric Hammond | Comments (3)</dd>
-->
            <dd class="entry-meta"></dd>
        
    
        
            <dt><a href="http://alestic.com/2013/08/awscli">Installing aws-cli, the New AWS Command Line Tool</a></dt>
            <dd>consistent control over more AWS services with aws-cli, a single, powerful command line tool from Amazon Readers of this tech blog know that I am a fan of the power&hellip;</dd>
<!-- 
            <dd class="entry-meta">By Eric Hammond | Comments (6)</dd>
-->
            <dd class="entry-meta"></dd>
        
    
        
            <dt><a href="http://alestic.com/2013/07/cloudformation-gmail-dash">Using An AWS CloudFormation Stack To Allow "-" Instead Of "+" In Gmail Email Addresses</a></dt>
            <dd>Launch a CloudFormation template to set up a stack of AWS resources to fill a simple need: Supporting Gmail addresses with &#8220;-&#8221; instead of &#8220;+&#8221; separating the user name from&hellip;</dd>
<!-- 
            <dd class="entry-meta">By Eric Hammond | Comments (0)</dd>
-->
            <dd class="entry-meta"></dd>
        
    
        
            <dt><a href="http://alestic.com/2013/07/ec2-expire-snapshots-v011">New Options In ec2-expire-snapshots v0.11</a></dt>
            <dd>The ec2-expire-snapshots program can be used to expire EBS snapshots in Amazon EC2 on a regular schedule that you define. It can be used as a companion to ec2-consistent-snapshot or&hellip;</dd>
<!-- 
            <dd class="entry-meta">By Eric Hammond | Comments (4)</dd>
-->
            <dd class="entry-meta"></dd>
        
    
        
            <dt><a href="http://alestic.com/2013/03/cloudfront-invalidation">Replacing a CloudFront Distribution to "Invalidate" All Objects</a></dt>
            <dd>I was chatting with Kevin Boyd (aka Beryllium) on the ##aws Freenode IRC channel about the challenge of invalidating a large number of CloudFront objects (35,000) due to a problem&hellip;</dd>
<!-- 
            <dd class="entry-meta">By Eric Hammond | Comments (4)</dd>
-->
            <dd class="entry-meta"></dd>
        
    
        
            <dt><a href="http://alestic.com/2013/01/aws-billing-alerts">Email Alerts for AWS Billing Alarms</a></dt>
            <dd>using CloudWatch and SNS to send yourself email messages when AWS costs accrue past limits you define The Amazon documentation describes how to use the AWS console to monitor your&hellip;</dd>
<!-- 
            <dd class="entry-meta">By Eric Hammond | Comments (2)</dd>
-->
            <dd class="entry-meta"></dd>
        
    
        
            <dt><a href="http://alestic.com/2012/12/s3-glacier-costs">Cost of Transitioning S3 Objects to Glacier</a></dt>
            <dd>how I was surprised by a large AWS charge and how to calculate the break-even point Glacier Archival of S3 Objects Amazon recently introduced a fantastic new feature where S3&hellip;</dd>
<!-- 
            <dd class="entry-meta">By Eric Hammond | Comments (10)</dd>
-->
            <dd class="entry-meta"></dd>
        
    
        
            <dt><a href="http://alestic.com/2012/11/ec2-sydney-australia">Running Ubuntu on Amazon EC2 in Sydney, Australia</a></dt>
            <dd>Amazon has announced a new AWS region in Sydney, Australia with the name ap-southeast-2. The official Ubuntu AMI lookup pages (1, 2) don&#8217;t seem to be showing the new location&hellip;</dd>
<!-- 
            <dd class="entry-meta">By Eric Hammond | Comments (0)</dd>
-->
            <dd class="entry-meta"></dd>
        
    
        
            <dt><a href="http://alestic.com/2012/09/ec2-reserved-instance-savings">Save Money by Giving Away Unused Heavy Utilization Reserved Instances</a></dt>
            <dd>You may be able to save on future EC2 expenses by selling an unused Reserved Instance for less than its true value or even $0.01, provided it is in the&hellip;</dd>
<!-- 
            <dd class="entry-meta">By Eric Hammond | Comments (5)</dd>
-->
            <dd class="entry-meta"></dd>
        
    
        
            <dt><a href="http://alestic.com/2012/09/aws-command-line-tools">Installing AWS Command Line Tools from Amazon Downloads</a></dt>
            <dd> This article describes how to install the old generation of AWS command line tools. For the most part, these have been replaced with the new AWS cli that is&hellip;</dd>
<!-- 
            <dd class="entry-meta">By Eric Hammond | Comments (9)</dd>
-->
            <dd class="entry-meta"></dd>
        
    
        
            <dt><a href="http://alestic.com/2012/08/ec2-provisioned-iops-ebs">Convert Running EC2 Instance to EBS-Optimized Instance with Provisioned IOPS EBS Volumes</a></dt>
            <dd>Amazon just announced two related features for getting super-fast, consistent performance with EBS volumes: (1) Provisioned IOPS EBS volumes, and (2) EBS-Optimized Instances. Starting new instances and EBS volumes with&hellip;</dd>
<!-- 
            <dd class="entry-meta">By Eric Hammond | Comments (0)</dd>
-->
            <dd class="entry-meta"></dd>
        
    
        
            <dt><a href="http://alestic.com/2012/06/ec2-outage-availability-zone">Which EC2 Availability Zone is Affected by an Outage?</a></dt>
            <dd>Did you know that Amazon includes status messages about the health of availability zones in the output of the ec2-describe-availability-zones command, the associated API call, and the AWS console? Right&hellip;</dd>
<!-- 
            <dd class="entry-meta">By Eric Hammond | Comments (5)</dd>
-->
            <dd class="entry-meta"></dd>
        
    
        
            <dt><a href="http://alestic.com/2012/05/aws-command-line-packages">Installing AWS Command Line Tools Using Ubuntu Packages</a></dt>
            <dd>See also: Installing AWS Command Line Tools from Amazon Downloads Here are the steps for installing the AWS command line tools that are currently available as Ubuntu packages. These include:&hellip;</dd>
<!-- 
            <dd class="entry-meta">By Eric Hammond | Comments (11)</dd>
-->
            <dd class="entry-meta"></dd>
        
    
        
            <dt><a href="http://alestic.com/2012/04/ubuntu-uds">Ubuntu Developer Summit, May 2012 (Oakland)</a></dt>
            <dd>I will be attending the Ubuntu Developer Summit (UDS) next week in Oakland, CA.  This event brings people from around the world together in one place every six months to&hellip;</dd>
<!-- 
            <dd class="entry-meta">By Eric Hammond | Comments (0)</dd>
-->
            <dd class="entry-meta"></dd>
        
    
        
            <dt><a href="http://alestic.com/2012/04/ec2-ssh-host-key">Uploading Known ssh Host Key in EC2 user-data Script</a></dt>
            <dd>The ssh protocol uses two different keys to keep you secure: The user ssh key is the one we normally think of. This authenticates us to the remote host, proving&hellip;</dd>
<!-- 
            <dd class="entry-meta">By Eric Hammond | Comments (2)</dd>
-->
            <dd class="entry-meta"></dd>
        
    
        
            <dt><a href="http://alestic.com/2012/04/aws-s3-torrent">Seeding Torrents with Amazon S3 and s3cmd on Ubuntu</a></dt>
            <dd>Amazon Web Services is such a huge, complex service with so many products and features that sometimes very simple but powerful features fall through the cracks when you&#8217;re reading the&hellip;</dd>
<!-- 
            <dd class="entry-meta">By Eric Hammond | Comments (3)</dd>
-->
            <dd class="entry-meta"></dd>
        
    
        
            <dt><a href="http://alestic.com/2012/03/cloudcamp">CloudCamp</a></dt>
            <dd>There are a number of CloudCamp events coming up in cities around the world. These are free events, organized around the various concepts, technologies, and services that fall under the&hellip;</dd>
<!-- 
            <dd class="entry-meta">By Eric Hammond | Comments (0)</dd>
-->
            <dd class="entry-meta"></dd>
        
    
        
            <dt><a href="http://alestic.com/2012/03/ec2-64-bit">Use the Same Architecture (64-bit) on All EC2 Instance Types</a></dt>
            <dd>A few hours ago, Amazon AWS announced that all EC2 instance types can now run 64-bit AMIs. Though t1.micro, m1.small, and c1.medium will continue to also support 32-bit AMIs, it&hellip;</dd>
<!-- 
            <dd class="entry-meta">By Eric Hammond | Comments (14)</dd>
-->
            <dd class="entry-meta"></dd>
        
    
        
            <dt><a href="http://alestic.com/2012/02/ec2-consistent-snapshot-on-github">ec2-consistent-snapshot on GitHub and v0.43 Released</a></dt>
            <dd>The source for ec2-conssitent-snapshot has historically been available here: ec2-consistent-snapshot on Launchpad.net using Bazaar For your convenience, it is now also available here: ec2-consistent-snapshot on GitHub using Git You are&hellip;</dd>
<!-- 
            <dd class="entry-meta">By Eric Hammond | Comments (6)</dd>
-->
            <dd class="entry-meta"></dd>
        
    
        
            <dt><a href="http://alestic.com/2012/01/ec2-ebs-boot-recommended">You Should Use EBS Boot Instances on Amazon EC2</a></dt>
            <dd>EBS boot vs. instance-store If you are just getting started with Amazon EC2, then use EBS boot instances and stop reading this article. Forget that you ever heard about instance-store&hellip;</dd>
<!-- 
            <dd class="entry-meta">By Eric Hammond | Comments (23)</dd>
-->
            <dd class="entry-meta"></dd>
        
        </dl>
    </div>
</div>
        
    


<div class="widget-archive-monthly widget-archive widget">
    <h3 class="widget-header">Monthly <a href="http://alestic.com/archives.html">Archives</a></h3>
    <div class="widget-content">
        <ul>
        
            <li><a href="http://alestic.com/2015/04/">April 2015 (2)</a></li>
        
    
        
            <li><a href="http://alestic.com/2014/12/">December 2014 (3)</a></li>
        
    
        
            <li><a href="http://alestic.com/2014/11/">November 2014 (5)</a></li>
        
    
        
            <li><a href="http://alestic.com/2014/09/">September 2014 (2)</a></li>
        
    
        
            <li><a href="http://alestic.com/2014/06/">June 2014 (1)</a></li>
        
    
        
            <li><a href="http://alestic.com/2014/02/">February 2014 (1)</a></li>
        
    
        
            <li><a href="http://alestic.com/2014/01/">January 2014 (3)</a></li>
        
    
        
            <li><a href="http://alestic.com/2013/12/">December 2013 (2)</a></li>
        
    
        
            <li><a href="http://alestic.com/2013/11/">November 2013 (1)</a></li>
        
    
        
            <li><a href="http://alestic.com/2013/09/">September 2013 (1)</a></li>
        
    
        
            <li><a href="http://alestic.com/2013/08/">August 2013 (1)</a></li>
        
    
        
            <li><a href="http://alestic.com/2013/07/">July 2013 (2)</a></li>
        
    
        
            <li><a href="http://alestic.com/2013/03/">March 2013 (1)</a></li>
        
    
        
            <li><a href="http://alestic.com/2013/01/">January 2013 (1)</a></li>
        
    
        
            <li><a href="http://alestic.com/2012/12/">December 2012 (1)</a></li>
        
    
        
            <li><a href="http://alestic.com/2012/11/">November 2012 (1)</a></li>
        
    
        
            <li><a href="http://alestic.com/2012/09/">September 2012 (2)</a></li>
        
    
        
            <li><a href="http://alestic.com/2012/08/">August 2012 (1)</a></li>
        
    
        
            <li><a href="http://alestic.com/2012/06/">June 2012 (1)</a></li>
        
    
        
            <li><a href="http://alestic.com/2012/05/">May 2012 (1)</a></li>
        
    
        
            <li><a href="http://alestic.com/2012/04/">April 2012 (3)</a></li>
        
    
        
            <li><a href="http://alestic.com/2012/03/">March 2012 (2)</a></li>
        
    
        
            <li><a href="http://alestic.com/2012/02/">February 2012 (1)</a></li>
        
    
        
            <li><a href="http://alestic.com/2012/01/">January 2012 (1)</a></li>
        
    
        
            <li><a href="http://alestic.com/2011/12/">December 2011 (1)</a></li>
        
    
        
            <li><a href="http://alestic.com/2011/11/">November 2011 (2)</a></li>
        
    
        
            <li><a href="http://alestic.com/2011/10/">October 2011 (2)</a></li>
        
    
        
            <li><a href="http://alestic.com/2011/09/">September 2011 (2)</a></li>
        
    
        
            <li><a href="http://alestic.com/2011/08/">August 2011 (3)</a></li>
        
    
        
            <li><a href="http://alestic.com/2011/06/">June 2011 (2)</a></li>
        
    
        
            <li><a href="http://alestic.com/2011/04/">April 2011 (4)</a></li>
        
    
        
            <li><a href="http://alestic.com/2011/03/">March 2011 (1)</a></li>
        
    
        
            <li><a href="http://alestic.com/2011/02/">February 2011 (4)</a></li>
        
    
        
            <li><a href="http://alestic.com/2010/12/">December 2010 (2)</a></li>
        
    
        
            <li><a href="http://alestic.com/2010/10/">October 2010 (6)</a></li>
        
    
        
            <li><a href="http://alestic.com/2010/09/">September 2010 (4)</a></li>
        
    
        
            <li><a href="http://alestic.com/2010/08/">August 2010 (2)</a></li>
        
    
        
            <li><a href="http://alestic.com/2010/05/">May 2010 (2)</a></li>
        
    
        
            <li><a href="http://alestic.com/2010/04/">April 2010 (3)</a></li>
        
    
        
            <li><a href="http://alestic.com/2010/03/">March 2010 (2)</a></li>
        
    
        
            <li><a href="http://alestic.com/2010/02/">February 2010 (3)</a></li>
        
    
        
            <li><a href="http://alestic.com/2010/01/">January 2010 (8)</a></li>
        
    
        
            <li><a href="http://alestic.com/2009/12/">December 2009 (3)</a></li>
        
    
        
            <li><a href="http://alestic.com/2009/11/">November 2009 (4)</a></li>
        
    
        
            <li><a href="http://alestic.com/2009/10/">October 2009 (4)</a></li>
        
    
        
            <li><a href="http://alestic.com/2009/09/">September 2009 (2)</a></li>
        
    
        
            <li><a href="http://alestic.com/2009/08/">August 2009 (6)</a></li>
        
    
        
            <li><a href="http://alestic.com/2009/07/">July 2009 (2)</a></li>
        
    
        
            <li><a href="http://alestic.com/2009/06/">June 2009 (11)</a></li>
        
    
        
            <li><a href="http://alestic.com/2009/05/">May 2009 (4)</a></li>
        
    
        
            <li><a href="http://alestic.com/2009/04/">April 2009 (4)</a></li>
        
    
        
            <li><a href="http://alestic.com/2009/03/">March 2009 (1)</a></li>
        
    
        
            <li><a href="http://alestic.com/2009/02/">February 2009 (1)</a></li>
        
    
        
            <li><a href="http://alestic.com/2008/12/">December 2008 (2)</a></li>
        
    
        
            <li><a href="http://alestic.com/2008/11/">November 2008 (1)</a></li>
        
    
        
            <li><a href="http://alestic.com/2008/10/">October 2008 (2)</a></li>
        
    
        
            <li><a href="http://alestic.com/2008/09/">September 2008 (1)</a></li>
        
    
        
            <li><a href="http://alestic.com/2008/08/">August 2008 (2)</a></li>
        
    
        
            <li><a href="http://alestic.com/2008/05/">May 2008 (3)</a></li>
        
    
        
            <li><a href="http://alestic.com/2008/04/">April 2008 (4)</a></li>
        
    
        
            <li><a href="http://alestic.com/2007/11/">November 2007 (1)</a></li>
        
        </ul>
    </div>
</div>
        
    



    </div>
</div>



                </div>
            </div>
            <div id="footer">
                <div id="footer-inner">
                    <div id="footer-content">
Copyright &copy;2007-2015 <a href="http://www.anvilon.com/">Eric Hammond</a>


                    </div>
                </div>
            </div>
        </div>
    </div>

<!-- Google +1 -->
<script type="text/javascript">
  (function() {
    var po = document.createElement('script'); po.type = 'text/javascript'; po.async = true;
    po.src = 'https://apis.google.com/js/plusone.js';
    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(po, s);
  })();
</script>
</body>
</html>
"""
