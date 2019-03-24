var mod = angular.module("yoFeul")

mod.factory('loginService', function ($http, server_url) {
    var info = {};

    info.username = null;
    info.password = null;
    info.key = null;
    info.loggedIn = false;

    info.login = function (user, pass) {
        var req = {
            method: 'POST',
            dataType: 'json',
            url: server_url + '/function/login',
            data: { 'username': user, 'password': pass, 'key': '' }
        };
        return $http(req)
    };

    return info;
})


mod.factory('registerService', function ($http, server_url){
    var info = {};

    
    info.register = function(user, pass, conf){
        var req = {
            method: 'POST',
            dataType: 'json',
            url: server_url + '/function/registerUser',
            data: { 'username': user, 'password': pass, 'key': ''}
        };

        return $http(req)
    }

    return info;
})