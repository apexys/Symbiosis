var useful = {};

/*useful.log = console.log;*/

useful.debug = false;

useful.byId = document.getElementById;

useful.post = function(path, data, callback_s, callback_f) {
    var headers = useful.multipart(data);
    var req = new XMLHttpRequest();
    req.open("POST", path, true);
    req.setRequestHeader("Content-Type", headers.contentTypeHeader);
    req.send(headers.encodedData);
    req.onreadystatechange = function(){
        if (req.readyState == 4 && req.status == 200){
            callback_s(req);}
        else{
            callback_f(req);}
        }
    };

useful.multipart = function(data) {
    var boundary = "wowSuch1337h4xXx";
    var ctHeader = "multipart/form-data; boundary=" + boundary;
    var encoded = "";
    for (x in data) {
        encoded += "--" + boundary + '\r\nContent-Disposition: form-data; name="' + x + '"\r\n\r\n' + data[x] + "\r\n";}
    encoded += "--" + boundary + "--\r\n";
    console.log(encoded);
    return {"contentTypeHeader": ctHeader, "encodedData": encoded};}
    
    
