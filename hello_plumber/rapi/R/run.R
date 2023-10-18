#' @export
run <- function(port = 8000) {
  script_path <- system.file("api", "api.R", package = "rapi")
  if (script_path == "") {
    stop("API script not found.")
  }

  plumber::pr(script_path) %>%
  plumber::pr_run(port = port)
}
