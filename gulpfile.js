const autoprefixer = require("gulp-autoprefixer");
const cssnano = require("cssnano")
const gulp = require("gulp");
const merge = require('merge-stream');
const moduleImporter = require("sass-module-importer");
const postcss = require("gulp-postcss")
const purgecss = require("gulp-purgecss");
const sass = require("gulp-sass");
const spritesmith = require('gulp.spritesmith');

const NODE_ENV = process.env.NODE_ENV || "develop"
const isProduction = NODE_ENV === "production"

const sassOptions = {
  errLogToConsole: true,
  outputStyle: "expanded",
  sourceMap: true,
  importer: moduleImporter(),
};

sass.compiler = require("node-sass");

const dest = "./director/assets/css";

const sassBuild = function () {

  const overrides = isProduction ? { outputStyle: "compressed" } : {}
  
  let stream = gulp
    .src("director/assets/sass/**/*.sass")
    .pipe(sass({ ...sassOptions, ...overrides }).on("error", sass.logError))
    .pipe(autoprefixer())

  if(isProduction) {
    stream = stream
      .pipe(purgecss({
        content: [
          './director/**/*.html',
          './director/assets/js/*.js'
        ],
      }))
      .pipe(postcss([cssnano()]))
  }

  return stream.pipe(gulp.dest(dest));
};

const watch = function (done) {
  gulp.watch(
    [
      "director/assets/sass/**/*.sass",
      "!director/assets/sass/sprites/_sprites.sass"
    ],
    { ignoreInitial: false },
    gulp.series(sprites, sassBuild)
  );
  done();
};

const sprites = function() {
  var spriteData = gulp
      .src([
        './director/assets/img/*-logo.png'
      ])
      .pipe(spritesmith({
          imgName: '../img/sprite.png',
          cssName: '_sprites.sass'
      }));

  var imgStream = spriteData.img
      .pipe(gulp.dest('./director/assets/img'));
  
  var cssStream = spriteData.css
  .pipe(gulp.dest('./director/assets/sass/sprites'));

  return merge(cssStream, imgStream);
}

exports.build = gulp.series(sprites, sassBuild);
exports.default = watch;
exports.watch = watch;
