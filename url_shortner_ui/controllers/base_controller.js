var HttpStatus = require('http-status-codes');
var redis = require('redis');
var client = redis.createClient();
var async = require('async');
var path = require('path');


exports.index_shurl = function(req,res){
	res.sendFile(path.resolve(__dirname+'/../static/templates/index.html'));
}