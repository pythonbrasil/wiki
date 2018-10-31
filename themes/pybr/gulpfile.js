var gulp      = require('gulp'),
    sass      = require('gulp-sass'),
    prefix    = require('gulp-autoprefixer'),
    notify    = require('gulp-notify'),
    cleanCSS  = require('gulp-clean-css'),
    minifyJS  = require('gulp-minify'),
    rename    = require('gulp-rename'),
    sync      = require('browser-sync');

gulp.task('scss', gulp.series(function (done) {
  gulp.src('./static/scss/pybr.scss')
    .pipe(sass({ errLogToConsole: true  }))
    .pipe(prefix())
    .pipe(cleanCSS({level: 2, inline: ['all']}))
    .pipe(rename({extname: '.min.css'}))
    .pipe(gulp.dest('./static/css'))
    .pipe(notify("styles compiled"))
    .pipe(sync.reload({ stream: true }));
  done();
}));

gulp.task('js', gulp.series(function (done) {
  gulp.src(['./node_modules/jquery/dist/jquery.min.js',
            './node_modules/tether/dist/js/tether.min.js',
            './node_modules/bootstrap/dist/js/bootstrap.min.js'])
    .pipe(gulp.dest('./static/js'))
    .pipe(notify("javascript updated"));
  done();
}));

gulp.task('fonts', gulp.series(function (done) {
  gulp.src('./node_modules/font-awesome/fonts/*')
    .pipe(gulp.dest('./static/fonts'))
    .pipe(notify("fonts updated"));
  done();
}));

gulp.task('sync', gulp.series(function(done) {
  sync.init({
    proxy: 'localhost:8000'
  });
  gulp.watch('./static/scss/**/*.scss', gulp.series(['scss']));
  gulp.watch('./static/js/**/*.js', gulp.series(sync.reload));
  done();
}));

gulp.task('build', gulp.series(['scss', 'js', 'fonts']));
gulp.task('default', gulp.series(['build', 'sync']));
