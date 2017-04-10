/**
 * Created by jerry on 005/2017/4/5.
 */
$(function () {
    var editor = editormd("vLargeTextField", {
        width: "70%",
        height: 640,
        syncScrolling: "single",
        path: "/static/editormd/lib/" // Autoload modules mode, codemirror, marked... dependents libs path
    });
});