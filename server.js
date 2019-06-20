var sys = require('util'),
    http = require('http'),
    url = require('url');

function notFound(res){
	res.writeHead(404, "text/plain");
	res.end("404: File not found");
}

http.createServer(function(b_req, b_res){
	console.log("Proxying request...");

	var b_url = url.parse(b_req.url, true);
	console.log(b_req.url);

	if(!b_url.query || !b_url.query.url) return notFound(b_res);

	var p_url = url.parse(b_url.query.url);
	console.log("requesting resource at :" + JSON.stringify(p_url));
	var options = {
		port   : p_url.port || 80,
		host   : p_url.href || 'localhost',
		method : p_url.type || 'GET',
		path   : p_url.pathname || '/'
	}

	var p_client = http.request(options);

	p_client.end();

	p_client.addListener('response', function(p_res){
		b_res.writeHead(p_res.statusCode, p_res.headers);
		p_res.addListener('data', function(chunk){
			b_res.write(chunk);
		});

		p_res.addListener('end', function(){
			b_res.end();
		});
	});
}).listen(9000, "127.0.0.1");
