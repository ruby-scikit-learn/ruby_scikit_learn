# -*- encoding: utf-8 -*-
lib = File.expand_path('../lib', __FILE__)
$LOAD_PATH.unshift(lib) unless $LOAD_PATH.include?(lib)
require 'ruby_scikit_learn/version'

Gem::Specification.new do |gem|
  gem.name          = "ruby_scikit_learn"
  gem.version       = RubyScikitLearn::VERSION
  gem.authors       = ["Andreas Hjortgaard Danielsen"]
  gem.email         = ["andreashd@gmail.com"]
  gem.description   = "Ruby wrapper for scikit-learn"
  gem.summary       = "Ruby wrapper for scikit-learn"
  gem.homepage      = ""

  gem.files         = `git ls-files`.split($/)
  gem.executables   = gem.files.grep(%r{^bin/}).map{ |f| File.basename(f) }
  gem.test_files    = gem.files.grep(%r{^(test|spec|features)/})
  gem.require_paths = ["lib"]

  gem.add_development_dependency "rake"
  gem.add_development_dependency "rspec"
end
