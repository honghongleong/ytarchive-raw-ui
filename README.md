# ytarchive-raw-ui

## Dependencies

- ffmpeg
- python3 > 3.4
- [ytarchive-raw](https://github.com/lekoOwO/ytarchive-raw)

## Only multi thread works for now.
To enable tempoarydir location and output location<br />
Add ```"-td",configuration["tempdir"],"-o",configuration["output"]``` to ```subprocess.call``` on line 64<br />
Thinking of ways to add other parameters onto subprocess<br />
First time coding python so dun expect much

## Usage
- Get freg json file
- `python ui.py`
- no to update config file
- yes if using .json(make sure json in same dir)<br />
->filename.json
- no if using url<br />
->Video url<br />
->Audio url
  
## Initial setup
```
1.Enter amount of threads
2.Enter output location
3.Enter tempoary directory
```
