require "rubygems"

desc "Deploy to Github Pages"
task :deploy, [:arg1] do |t, args|
  puts "## Deploying to Github Pages"

  system "git add ."

  message = "#{Time.now.utc} #{args[:arg1]}"
  puts "## Commiting: #{message}"
  system "git commit -m \"#{message}\""

  puts "## Pushing generated site"
  system "git push"

  puts "## Deploy Complete!"

  puts "## Deploy Complete!"
end