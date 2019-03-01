angular.module("yoFeul")
    .controller("signInCtrl", function ($scope) {
        $scope.user;

        $scope.verifyUsername = function () {
            if ($scope.user) {
                $scope.$parent.setUsername($scope.user);
                window.location = '#!user/profile'
            } else {
                window.location = '#!login'
            }
            console.log($scope.$parent.username)
        }
    });