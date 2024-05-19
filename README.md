Work in progress :)

Track progress made in R5_reloaded's aimtrainer based on the created logs per session.

## General instructions ##
 - Make sure to save sessions after finishing playing
 - Logs are processed based on which guns are used (hard coded in the beginning, will implement some kind of config option later)
    - Alternator -> hipfire
    - Hitscan single -> hipfire on frenzy?

## Requirements ##
 - Windows OS
 - Python installed ```3.11.0``` or newer recommended, might work on older versions, but software was developed on ```3.11.0```

## How to run ##
 - Clone repository
 - Navigate to repository
 - Create fle called: ```.env```
 - Add R5_Reloaded training logs file path to .env see ```example.env``` for reference
 - Run ```tracker.bat```
