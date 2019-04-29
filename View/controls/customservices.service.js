var mod = angular.module("yoFeul")

mod.factory('loginService', function ($http, server_url) {
    var info = {};

    info.id = null;
    info.username = null;
    info.password = null;
    info.key = null;
    info.loggedIn = false;
    info.type = null;

    info.login = function (user, pass) {
        user = 'username_01'
        pass = 'password_01'
        var req = {
            method: 'POST',
            dataType: 'json',
            url: server_url + '/function/login',
            data: { 'username': user, 'password': pass, 'key': '' }
        };
        return $http(req);
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

        return $http(req);
    }

    return info;
})

mod.factory('requestService', function ($http, server_url, loginService){
    var info = {};

    
    info.send = function(req_name, data_j){
        data_j.key = loginService.key;
        data_j.password = loginService.password;
        data_j.username = loginService.username;
        data_j.id = loginService.id;
        var req = {
            method: 'POST',
            dataType: 'json',
            url: server_url + '/function/' + req_name,
            data: data_j
        };

        return $http(req);
    }

    return info;
})