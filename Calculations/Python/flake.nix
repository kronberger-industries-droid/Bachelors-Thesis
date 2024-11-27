{
  description = "python environment for my bachelors thesis";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";
  };
  outputs = { self, nixpks }:
  let
    system = "x86_64-linux";
    pkgs = nixpks.LegacyPackages.${system};
  in
  {
    devShells.${system}.default =
      pkgs.mkShell
        {
          buildInputs = [
            (pkgs.python3.withPackages ( python-pkgs: with python-pkgs; [
              numpy
              matplotlib
              python-lsp-server
            ]))
          ];
        };
  };
    
}
