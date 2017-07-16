{ pkgs ? import <nixpkgs> { }, local ? true }:

with pkgs.python3Packages;
buildPythonPackage rec {
  pname = "tarjan";
  version = "0.0.1";
  name = "${pname}-${version}";
  src = ./. + (if local then "/dist/${name}.tar.gz" else "/${name}.tar.gz");
}
  
