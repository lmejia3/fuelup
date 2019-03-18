angular.module("yoFeul")
    .controller("signInCtrl", function ($scope, $http) {
        $scope.user;
        $scope.pass;

        $scope.verifyUsername = function () {

            var req = {
                method: 'GET',
                url: 'https://18.216.110.220/function/login',
                params: {username: $scope.user, password: $scope.pass}
            }

            $http(req).then(
                function(response){
                    console.log(response);
                    console.log('request successful');
                },
                function (response){
                    console.log(response);
                    console.log('request failed');
                }
            );


            if ($scope.user) {
                $scope.$parent.setUsername($scope.user);
                window.location = '#!user/profile'
            } else {
                window.location = '#!login'
            }
            console.log($scope.$parent.username);
        }
    });