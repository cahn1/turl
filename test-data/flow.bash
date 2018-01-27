
request comes: orig_url (long)
check_valid_url(orig_url)

#POST
if url dont contain 'rango.intuit.com' -> it means POST
  if not POST
    print Error
    exit 1
  else
    if orig_url exists then
      return short_url
    else
      increase id++
      put_item to table
      return short_url

#GET
else -> it means GET
  if not GET
    print error
    exirt 1
  else
    strip only short_url
    query table with short_url
    return orig_url



complete POST
complete GET
backup codes -> Trim codes
Build request/response with web UI

upload the code to github.com
create codebuild
add build status into github.com
customize codebuild
create code pipeline
 - dev, stg, prod
