var mod = angular.module("yoFeul")

mod.factory('loginService', function ($http) {
    var info = {};

    info.username = null;
    info.password = null;
    info.key = null;
    info.loggedIn = false;

    info.login = function (user, pass) {

        var req = {
            method: 'POST',
            dataType: 'json',
            url: 'http://18.216.110.220:20000/function/login',
            data: { 'username': user, 'password': pass, 'key': '' },
        };

        $http(req).then(
            function (response) {
                console.log('successful responce');
                console.log(response);
                data = JSON.parse(response.data)
                console.log(typeof(data))
            },
            function (response) {
                console.log('failed responce');
                console.log(response);
            }
        );


    };

    return info;
})