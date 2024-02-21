provider "http" {
}

data "http" "api_url" {
  url = "${var.subnet}${var.mask}/${var.base}"
  method = " "
}
