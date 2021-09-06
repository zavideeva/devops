resource "aws_key_pair" "instance_key" {
  key_name   = "ansible"
  public_key = file("./keys/id_rsa.pub")
}

resource "aws_instance" "app_server" {
  ami                    = "ami-0194c3e07668a7e36"
  instance_type          = "t2.micro"
  vpc_security_group_ids = [aws_security_group.ssh.id, aws_security_group.http.id]
  key_name               = aws_key_pair.instance_key.key_name

  tags = {
    Name = "ExampleAppServerInstance"
  }
}
