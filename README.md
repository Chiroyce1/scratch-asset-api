# scratch-asset-api

## A recreation of Scratch's assets server, thats it.


## Documentation

### I've tried to recreate `https://assets.scratch.mit.edu` as much as possible, so here goes

## Uploading Files
**All file formats are allowed**

To upload, send a POST request to `/{MD5}.{file_format}`, where `{MD5}` is the MD5 hash of the file
and `{file_format}` is the file extension of the uploaded file. For example:

`POST` `/2ab8ef08a9e38b5537adae7f94e4227e.txt`

and the request body has to be the file (not sure how exactly it is, but it seems to be some sort of raw binary of the file)

### Response
Will contain JSON, there will be a `status` key, and if it's value is `ok`, then all went well.
There is also `content-name` key, and it's value will be `/{MD5}.{file_format}` of the file you just uploaded. 

## Downloading Files
Very simple, just `GET` `/{MD5}.{file_format}` where `{MD5}` is the MD5 hash of the file
and `{file_format}` is the file extension of the uploaded file. 

## Problems that this solves
You don't have to download each and every file, if it's a format that browsers can display, it will be shown without being downloaded.
And this also has a feature that can whitelist only certain file extensions (just in case).
