angular.module("yoFeul")
    .controller("signInCtrl", function ($scope, $http) {
        $scope.user;
        $scope.pass;


        $scope.verifyUsername = function () {

            var req = {
                method: 'POST',
                dataType: 'json',
                url: 'http://18.216.110.220:20000/function/login',
                data: {'username': $scope.user, 'password': $scope.pass, 'key': ''},
            };
            $http(req).then(
                function(response){
                    console.log('successful responce');
                    console.log(response);
                },
                function (response){
                    console.log('failed responce');
                    console.log(response);
                }
            );

            if ($scope.user) {
                $scope.$parent.setUsername($scope.user);
                window.location = '#!user/profile';
            } else {
                window.location = '#!login';
            }
            console.log($scope.$parent.username);
        }
    });