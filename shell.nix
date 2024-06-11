{ sources ? import nix/sources.nix }:
let nixpkgs = import sources.nixpkgs {};
in 
(nixpkgs.buildFHSUserEnv {
  name = "piphell";
  targetPkgs = pkgs: (with pkgs; [
    python312
    python312Packages.pip
    python312Packages.virtualenv
  ]);
  runScript = "bash";
}).env
