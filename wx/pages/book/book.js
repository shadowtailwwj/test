// pages/book/book.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    check: false
  },
  onLoad: function (options) {
    // 生命周期函数--监听页面加载
    check: (options.check == "false" ? false : true )
  },
  switch1Change: function (e) {
    // console.log('checkbox类型开关当前状态-----', e.detail.value)
    check: (e.detail.value == "true" ? true : false)
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
  
  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {
  
  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {
  
  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {
  
  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {
  
  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {
  
  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {
  
  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {
  
  }
})