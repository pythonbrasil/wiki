var gulp      = require('gulp'),
    sass      = require('gulp-sass'),
    prefix    = require('gulp-autoprefixer'),
    notify    = require('gulp-notify'),
    cleanCSS  = require('gulp-clean-css'),
    minifyJS  = require('gulp-minify'),
    rename    = require('gulp-rename'),
    sync      = require('browser-sync');

gulp.task('scss', function () {
  gulp.src('./static/scss/pybr.scss')
    .pipe(sass({ errLogToConsole: true  }))
    .pipe(prefix())
    .pipe(cleanCSS({level: 2, inline: ['all']}))
    .pipe(rename({extname: '.min.css'}))
    .pipe(gulp.dest('./static/css'))
    .pipe(notify("styles compiled"))
    .pipe(sync.reload({ stream: true }));
});

gulp.task('js', function () {
  gulp.src(['./node_modules/jquery/dist/jquery.min.js',
            './node_modules/tether/dist/js/tether.min.js',
            './node_modules/bootstrap/dist/js/bootstrap.min.js'])
    .pipe(gulp.dest('./static/js'))
    .pipe(notify("javascript updated"));
});

gulp.task('fonts', function () {
  gulp.src('./node_modules/font-awesome/fonts/*')
    .pipe(gulp.dest('./static/fonts'))
    .pipe(notify("fonts updated"));
});

gulp.task('sync', function() {
  sync.init({
    proxy: 'localhost:8000'
  });
  gulp.watch('./static/scss/**/*.scss', ['scss']);
  gulp.watch('./static/js/**/*.js', sync.reload);
});

gulp.task('build', ['scss', 'js', 'fonts']);
gulp.task('default', ['build', 'sync']);
