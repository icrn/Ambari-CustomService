# ambari自定义服务


### ambari自定义增加grafana
1. 下载官网rpm包增加至yum中，用yum list | grep grafana可以查看到
2. 把src下的GRAFANA文件整个扔到/var/lib/ambari-server/resources/stacks/HDP/3.1/services下
3. 执行ambari-server restart
详细参看 https://cwiki.apache.org/confluence/display/AMBARI/Defining+a+Custom+Service

### ambari自定义增加kibana
安装同上，但是kibana相对来说配置会复杂一点,建议安装kibana6.5以上版本，默认安装了x-pack安装会简单很多

### ambari自定义增加logstash
同上，安装即可用
