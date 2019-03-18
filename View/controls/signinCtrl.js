angular.module("yoFeul")
    .controller("signInCtrl", function ($scope) {
        $scope.user;
        $scope.user;

        $scope.verifyUsername = function () {

            var req = {
                method: 'GET',
                url: 'http://18.216.110.220:20000/function/login',
                params: {username: $scope.user, password: $scope.pass}
            }

            if ($scope.user) {
                $scope.$parent.setUsername($scope.user);
                window.location = '#!user/profile'
            } else {
                window.location = '#!login'
            }
            console.log($scope.$parent.username)
        }
    });