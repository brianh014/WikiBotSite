#!/usr/bin/python

import cgi
import cgitb; cgitb.enable()
import sys

print """
<!DOCTYPE html>
<html>
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
	<meta name="Keywords" content="wikipedia,wikibot,wiki,bot,reddit">
	<meta name="Description" content="Stats for WikiBot">
	<title>WikiBot Stats</title>
    
    <link rel="stylesheet" type="text/css" href="../style.css">
    
</head>

<body>
    
    <div class="navbar">
        <div style="margin-left:15px; padding-top:10px; font-size:25px; font-family:Arial;">
            <a href="../index.html" class="nav">Home</a>
            <a href="stats.py" class="nav">Stats</a>
            <a href="../faq.html" class="nav">FAQ</a>
        </div>
    </div>
    
    <div style="margin-top:20px; margin-bottom:20px; text-align:center">
        <img src="../art/wikibot_stats.png" alt="WikiBot faq" height=158 width=413 style="text-align:center;">
    </div>
    
    <div style="font-family:Arial; font-size:25px; text-align:center">
    
        <div>
            <b>Number of WikiBot calls</b>
            <p style="margin-top:5px">X</p>
        </div>
        
        <div style="width:30%; margin-left:15%; float:left; padding:20px;">
            <b>10 Most Recent Queries</b>
            <ol>
                <li>Test</li>
                <li>Test</li>
                <li>Test</li>
                <li>Test</li>
                <li>Test</li>
                <li>Test</li>
                <li>Test</li>
                <li>Test</li>
                <li>Test</li>
                <li>Test</li>
            </ol>
        </div>
            
        <div style="width:30%; margin-right:15%; float:right; padding:20px;">
            <b>Top 10 SubReddits</b>
            <ol>
                <li>Test</li>
                <li>Test</li>
                <li>Test</li>
                <li>Test</li>
                <li>Test</li>
                <li>Test</li>
                <li>Test</li>
                <li>Test</li>
                <li>Test</li>
                <li>Test</li>
            </ol>
        </div>
        
        <div style="width:30%; margin-left:15%; float:left; padding:20px;">
            <b>Some stats</b>
            <ol>
                <li>Test</li>
                <li>Test</li>
                <li>Test</li>
                <li>Test</li>
                <li>Test</li>
                <li>Test</li>
                <li>Test</li>
                <li>Test</li>
                <li>Test</li>
                <li>Test</li>
            </ol>
        </div>
        
        <div style="width:30%; margin-right:15%; float:right; padding:20px;">
            <b>Some other stats</b>
            <ol>
                <li>Test</li>
                <li>Test</li>
                <li>Test</li>
                <li>Test</li>
                <li>Test</li>
                <li>Test</li>
                <li>Test</li>
                <li>Test</li>
                <li>Test</li>
                <li>Test</li>
            </ol>
        </div>
        
    </div>
    
</body>
</html>
"""
